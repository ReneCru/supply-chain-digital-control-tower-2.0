"""Public portfolio contracts for the governed OTD recovery workflow."""

from dataclasses import dataclass
from datetime import date
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class DecisionStatus(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(frozen=True)
class DeliveryObservation:
    supplier_id: str
    order_id: str
    promised_date: date
    delivered_date: date

    @property
    def on_time(self) -> bool:
        return self.delivered_date <= self.promised_date


@dataclass(frozen=True)
class PerformanceResult:
    supplier_id: str
    total_deliveries: int
    on_time_deliveries: int
    otd: float


@dataclass(frozen=True)
class RiskAssessment:
    supplier_id: str
    level: RiskLevel
    reason: str


@dataclass(frozen=True)
class OperationalAlert:
    supplier_id: str
    title: str
    evidence: str


@dataclass(frozen=True)
class Recommendation:
    supplier_id: str
    action: str
    rationale: str


@dataclass(frozen=True)
class HumanDecision:
    supplier_id: str
    status: DecisionStatus
    decided_by: str
    note: str = ""


@dataclass(frozen=True)
class OutcomeMeasurement:
    supplier_id: str
    baseline_otd: float
    followup_otd: float

    @property
    def percentage_point_change(self) -> float:
        return round((self.followup_otd - self.baseline_otd) * 100, 2)
