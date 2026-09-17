# Technical Evidence Map

| Claim | Repository evidence |
|---|---|
| Deterministic supplier OTD calculation | `src/performance/otd.py` |
| Explicit business/domain contracts | `src/contracts/models.py` |
| Simplified portfolio risk assessment | `src/risk/portfolio.py` |
| Governed recommendation workflow | `src/workflow/recovery.py` |
| Human authority required before action | `authorize_action()` + workflow tests |
| Outcome change measured without automatic causation claim | `OutcomeMeasurement` + tests + `demo.py` |
| Relational persistence design | `db/schema.sql` |
| Synthetic-only demonstration data | `data/sample/deliveries.csv` |
| Automated behavioral validation | `tests/test_portfolio_workflow.py` |
| Continuous integration | `.github/workflows/ci.yml` |
| Public/private IP boundary | `docs/portfolio_boundary.md` |
| Security/disclosure policy | `SECURITY.md` |

This map is intentionally evidence-first: recruiter-facing claims should remain traceable to something inspectable in the Portfolio Edition.
