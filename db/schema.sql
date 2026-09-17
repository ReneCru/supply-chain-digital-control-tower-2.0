-- Portfolio Edition persistence schema.
-- Synthetic/demo architecture only; intentionally excludes private intelligence internals.

CREATE TABLE IF NOT EXISTS supplier_performance (
    performance_id BIGSERIAL PRIMARY KEY,
    supplier_id TEXT NOT NULL,
    measured_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    total_deliveries INTEGER NOT NULL CHECK (total_deliveries > 0),
    on_time_deliveries INTEGER NOT NULL CHECK (on_time_deliveries >= 0),
    otd NUMERIC(6,4) NOT NULL CHECK (otd BETWEEN 0 AND 1),
    CHECK (on_time_deliveries <= total_deliveries)
);

CREATE TABLE IF NOT EXISTS operational_alert (
    alert_id BIGSERIAL PRIMARY KEY,
    supplier_id TEXT NOT NULL,
    title TEXT NOT NULL,
    evidence TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS recommendation (
    recommendation_id BIGSERIAL PRIMARY KEY,
    supplier_id TEXT NOT NULL,
    action_text TEXT NOT NULL,
    rationale TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS human_decision (
    decision_id BIGSERIAL PRIMARY KEY,
    recommendation_id BIGINT NOT NULL REFERENCES recommendation(recommendation_id),
    decision_status TEXT NOT NULL CHECK (decision_status IN ('approved', 'rejected')),
    decided_by TEXT NOT NULL,
    decision_note TEXT NOT NULL DEFAULT '',
    decided_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS action_evidence (
    evidence_id BIGSERIAL PRIMARY KEY,
    decision_id BIGINT NOT NULL REFERENCES human_decision(decision_id),
    evidence_type TEXT NOT NULL,
    evidence_reference TEXT NOT NULL,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS outcome_measurement (
    outcome_id BIGSERIAL PRIMARY KEY,
    supplier_id TEXT NOT NULL,
    baseline_otd NUMERIC(6,4) NOT NULL CHECK (baseline_otd BETWEEN 0 AND 1),
    followup_otd NUMERIC(6,4) NOT NULL CHECK (followup_otd BETWEEN 0 AND 1),
    measured_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_performance_supplier
    ON supplier_performance (supplier_id, measured_at DESC);
CREATE INDEX IF NOT EXISTS idx_alert_supplier
    ON operational_alert (supplier_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_outcome_supplier
    ON outcome_measurement (supplier_id, measured_at DESC);
