"""Simplified public risk assessment.

The private development edition uses a richer governed policy model. The
thresholds below are illustrative portfolio values and are not copied from
private production-oriented intelligence logic.
"""

from src.contracts.models import PerformanceResult, RiskAssessment, RiskLevel


def assess_delivery_risk(result: PerformanceResult) -> RiskAssessment:
    """Translate OTD evidence into a simple demonstration risk signal."""
    if result.otd < 0.75:
        level = RiskLevel.HIGH
    elif result.otd < 0.90:
        level = RiskLevel.MEDIUM
    else:
        level = RiskLevel.LOW

    return RiskAssessment(
        supplier_id=result.supplier_id,
        level=level,
        reason=(
            f"Synthetic portfolio assessment based on OTD={result.otd:.1%}; "
            "illustrative thresholds only."
        ),
    )
