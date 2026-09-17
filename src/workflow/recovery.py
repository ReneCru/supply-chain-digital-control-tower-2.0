"""Governed public vertical slice from risk evidence to human decision."""

from src.contracts.models import (
    DecisionStatus,
    HumanDecision,
    OperationalAlert,
    Recommendation,
    RiskAssessment,
    RiskLevel,
)


def create_alert(risk: RiskAssessment) -> OperationalAlert | None:
    """Create attention signal for material portfolio risk."""
    if risk.level is RiskLevel.LOW:
        return None
    return OperationalAlert(
        supplier_id=risk.supplier_id,
        title="Supplier delivery performance requires review",
        evidence=risk.reason,
    )


def propose_recommendation(alert: OperationalAlert) -> Recommendation:
    """Return a deliberately generic public recommendation contract."""
    return Recommendation(
        supplier_id=alert.supplier_id,
        action="Review delivery-recovery options with the accountable owner",
        rationale=alert.evidence,
    )


def authorize_action(
    recommendation: Recommendation,
    decision: HumanDecision,
) -> str:
    """Enforce the human authority boundary before operational execution."""
    if decision.supplier_id != recommendation.supplier_id:
        raise ValueError("Decision and recommendation refer to different suppliers")
    if decision.status is not DecisionStatus.APPROVED:
        return "NO_ACTION_AUTHORIZED"
    return "HUMAN_APPROVED_ACTION_READY"
