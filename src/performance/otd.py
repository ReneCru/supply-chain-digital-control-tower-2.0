"""Representative deterministic On-Time Delivery calculation."""

from collections.abc import Iterable

from src.contracts.models import DeliveryObservation, PerformanceResult


def calculate_otd(
    supplier_id: str,
    observations: Iterable[DeliveryObservation],
) -> PerformanceResult:
    """Calculate supplier OTD from validated delivery observations.

    OTD = on-time deliveries / total deliveries.
    The calculation is deliberately deterministic and contains no AI logic.
    """
    supplier_rows = [row for row in observations if row.supplier_id == supplier_id]
    if not supplier_rows:
        raise ValueError(f"No delivery observations for supplier {supplier_id}")

    on_time = sum(row.on_time for row in supplier_rows)
    return PerformanceResult(
        supplier_id=supplier_id,
        total_deliveries=len(supplier_rows),
        on_time_deliveries=on_time,
        otd=round(on_time / len(supplier_rows), 4),
    )
