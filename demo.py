"""Run the public OTD recovery vertical slice with synthetic data."""

from datetime import date

from src.contracts.models import DecisionStatus, DeliveryObservation, HumanDecision, OutcomeMeasurement
from src.performance.otd import calculate_otd
from src.risk.portfolio import assess_delivery_risk
from src.workflow.recovery import authorize_action, create_alert, propose_recommendation


def main() -> None:
    supplier = "SYN-SUP-001"
    deliveries = [
        DeliveryObservation(supplier, "SYN-PO-1", date(2026, 1, 10), date(2026, 1, 10)),
        DeliveryObservation(supplier, "SYN-PO-2", date(2026, 1, 15), date(2026, 1, 17)),
        DeliveryObservation(supplier, "SYN-PO-3", date(2026, 1, 20), date(2026, 1, 20)),
        DeliveryObservation(supplier, "SYN-PO-4", date(2026, 1, 25), date(2026, 1, 27)),
    ]

    performance = calculate_otd(supplier, deliveries)
    risk = assess_delivery_risk(performance)
    alert = create_alert(risk)

    print(f"Supplier: {supplier}")
    print(f"Baseline OTD: {performance.otd:.1%}")
    print(f"Risk: {risk.level.value.upper()}")

    if alert is None:
        print("No material alert. Workflow ends without action.")
        return

    recommendation = propose_recommendation(alert)
    print(f"Recommendation: {recommendation.action}")

    # Explicit simulation of accountable human authority.
    decision = HumanDecision(
        supplier_id=supplier,
        status=DecisionStatus.APPROVED,
        decided_by="demo-human-reviewer",
        note="Synthetic portfolio demonstration only.",
    )
    authorization = authorize_action(recommendation, decision)
    print(f"Authorization: {authorization}")

    # Follow-up value is synthetic. Reporting change does not establish causation.
    outcome = OutcomeMeasurement(supplier, baseline_otd=0.72, followup_otd=0.84)
    print(
        "Synthetic outcome: "
        f"{outcome.baseline_otd:.0%} -> {outcome.followup_otd:.0%} "
        f"({outcome.percentage_point_change:+.1f} pp)"
    )
    print("Causation claim: NOT ESTABLISHED")


if __name__ == "__main__":
    main()
