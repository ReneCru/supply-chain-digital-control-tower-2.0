# Business Case — Supplier Delivery Recovery

## Problem

A supplier-performance dashboard can show that On-Time Delivery is deteriorating, but the KPI alone does not create operational recovery. Teams still need to identify material risk, document a recommendation, obtain accountable approval, coordinate corrective action, preserve execution evidence, and measure subsequent performance.

## Portfolio Scenario

This edition demonstrates a synthetic supplier delivery-recovery workflow:

1. Delivery observations are validated.
2. OTD is calculated deterministically.
3. Performance evidence produces a simplified risk signal.
4. A material condition can create an alert.
5. A recommendation contract records a proposed response and supporting evidence.
6. A human approves or rejects the proposal.
7. Approved work becomes a controlled action record.
8. Execution evidence is captured.
9. Later performance is measured against the baseline.

## Why Governance Matters

Operational automation becomes risky when detection, recommendation, authority, and execution are treated as the same thing. This project separates them.

```text
Intelligence to recommend ≠ authority to act
```

The architecture therefore treats human approval as a first-class business object rather than an informal step outside the system.

## Outcome Measurement

The project distinguishes correlation from causation. A completed action can be associated with a later KPI change, but the system should not automatically claim that the action caused the change without sufficient evidence.

A representative portfolio example can compare:

- baseline OTD;
- post-action OTD;
- absolute percentage-point change;
- target gap;
- action completion status;
- available execution evidence.

## Portfolio Value

The project demonstrates the ability to translate a business-operations problem into:

- measurable process logic;
- data contracts;
- deterministic calculations;
- automation boundaries;
- governance controls;
- persistence design;
- analytical outputs;
- automated validation.

The emphasis is not a dashboard alone. It is the controlled path from operational evidence to decision and measurable outcome.
