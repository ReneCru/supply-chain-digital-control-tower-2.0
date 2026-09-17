from datetime import date

import pytest

from src.contracts.models import (
    DecisionStatus,
    DeliveryObservation,
    HumanDecision,
    OutcomeMeasurement,
    RiskLevel,
)
from src.performance.otd import calculate_otd
from src.risk.portfolio import assess_delivery_risk
from src.workflow.recovery import authorize_action, create_alert, propose_recommendation


def _observations() -> list[DeliveryObservation]:
    return [
        DeliveryObservation("SYN-SUP-001", "PO-1", date(2026, 1, 10), date(2026, 1, 10)),
        DeliveryObservation("SYN-SUP-001", "PO-2", date(2026, 1, 12), date(2026, 1, 15)),
        DeliveryObservation("SYN-SUP-001", "PO-3", date(2026, 1, 20), date(2026, 1, 20)),
        DeliveryObservation("SYN-SUP-001", "PO-4", date(2026, 1, 25), date(2026, 1, 28)),
    ]


def test_otd_is_deterministic() -> None:
    result = calculate_otd("SYN-SUP-001", _observations())
    assert result.total_deliveries == 4
    assert result.on_time_deliveries == 2
    assert result.otd == 0.5


def test_missing_supplier_is_explicit_error() -> None:
    with pytest.raises(ValueError):
        calculate_otd("UNKNOWN", _observations())


def test_material_risk_creates_alert_and_recommendation() -> None:
    performance = calculate_otd("SYN-SUP-001", _observations())
    risk = assess_delivery_risk(performance)
    assert risk.level is RiskLevel.HIGH

    alert = create_alert(risk)
    assert alert is not None
    recommendation = propose_recommendation(alert)
    assert recommendation.supplier_id == "SYN-SUP-001"


def test_recommendation_cannot_authorize_itself() -> None:
    performance = calculate_otd("SYN-SUP-001", _observations())
    risk = assess_delivery_risk(performance)
    alert = create_alert(risk)
    assert alert is not None
    recommendation = propose_recommendation(alert)

    rejected = HumanDecision(
        supplier_id="SYN-SUP-001",
        status=DecisionStatus.REJECTED,
        decided_by="portfolio-reviewer",
    )
    assert authorize_action(recommendation, rejected) == "NO_ACTION_AUTHORIZED"

    approved = HumanDecision(
        supplier_id="SYN-SUP-001",
        status=DecisionStatus.APPROVED,
        decided_by="portfolio-reviewer",
    )
    assert authorize_action(recommendation, approved) == "HUMAN_APPROVED_ACTION_READY"


def test_outcome_reports_change_without_claiming_causation() -> None:
    outcome = OutcomeMeasurement(
        supplier_id="SYN-SUP-001",
        baseline_otd=0.72,
        followup_otd=0.84,
    )
    assert outcome.percentage_point_change == 12.0
