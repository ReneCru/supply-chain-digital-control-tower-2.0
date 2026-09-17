# Portfolio Architecture

## Purpose

This document describes the public, recruiter-facing architecture of Supply Chain Digital Control Tower 2.0. It intentionally excludes proprietary scoring thresholds, internal policy catalogs, advanced remediation playbooks, private orchestration details, and production integrations.

## Decision Lifecycle

The demonstrated architecture separates observation, analysis, decision, execution, and measurement.

```text
Observe → Measure → Assess → Alert → Recommend → Decide → Act → Evidence → Measure Outcome
```

This separation prevents dashboards from becoming hidden business-rule engines and preserves a clear human-control boundary.

## Layers

### 1. Operational Data
Synthetic delivery observations represent transactional supply-chain activity. The portfolio edition contains no real employer or supplier information.

### 2. Performance
Deterministic business calculations transform observations into reproducible KPIs. OTD is the representative KPI in this edition.

### 3. Risk
A simplified risk component converts performance evidence into a business risk signal. The public implementation demonstrates the pattern without exposing private thresholds or the complete intelligence model.

### 4. Alerting
Material signals can generate an operational alert. Alerts identify that attention is required; they do not authorize an action.

### 5. Recommendation Contract
The system can represent a proposed next action and the evidence supporting it. Private recommendation policies and advanced playbooks are outside the public repository.

### 6. Human Decision
A human decision record explicitly approves or rejects a proposed action. This is a deliberate governance boundary.

### 7. Action & Evidence
Approved decisions may create controlled action records. Completion evidence provides traceability between an approved decision and reported execution.

### 8. Outcome Measurement
The workflow measures subsequent business performance rather than assuming that an action caused improvement.

### 9. Persistence & Analytics
The design is PostgreSQL-oriented and separates operational records from analytical outputs. The portfolio schema is intentionally smaller than the private development architecture.

## Engineering Boundaries

- Business calculations should be deterministic and testable.
- Presentation should not own business logic.
- Persistence should be replaceable behind clear interfaces.
- Material actions require human authority.
- Events and evidence should support traceability.
- AI may assist interpretation in future extensions but does not replace deterministic controls or human authorization.

## Deliberately Excluded

The portfolio edition does not publish:

- proprietary policy thresholds;
- complete scenario-classification logic;
- full recommendation-engine internals;
- advanced remediation playbooks;
- predictive-intelligence implementation;
- AI-copilot internals;
- private decision-replay mechanisms;
- production ERP or supplier integrations.

These exclusions are intentional IP and confidentiality controls, not missing architectural awareness.
