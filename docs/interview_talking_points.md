# Interview Talking Points

## 20 seconds

I built a governed supply-chain decision-support portfolio that takes a supplier performance problem from operational data through deterministic OTD measurement, risk and alerting, a recommendation, explicit human approval, and outcome measurement. The point is to demonstrate how I connect business operations with data, automation, controls, and measurable outcomes.

## What I would emphasize technically

The core KPI calculation is deterministic and testable. The workflow deliberately separates a recommendation from authority to act. PostgreSQL models the decision/evidence lifecycle, and GitHub Actions validates the tests and synthetic end-to-end demo on every change.

## Why the public code is smaller than the full project

The recruiter-facing repository is intentionally curated. It demonstrates the architecture and representative implementation without publishing the complete intelligence, policy thresholds, remediation playbooks, or other differentiated private logic.

## What I would not claim

- that this Portfolio Edition is production deployed;
- that AI autonomously makes procurement decisions;
- that the synthetic outcome proves causation;
- that the public risk thresholds are production policies.
