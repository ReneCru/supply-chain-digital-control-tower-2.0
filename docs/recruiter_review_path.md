# Recruiter Review Path

For a fast technical review:

1. Read the root `README.md` for the business problem and architecture.
2. Run `python demo.py` to see the governed vertical slice.
3. Inspect `src/performance/otd.py` for deterministic KPI logic.
4. Inspect `src/workflow/recovery.py` for the human-authorization boundary.
5. Inspect `tests/test_portfolio_workflow.py` for behavioral validation.
6. Inspect `db/schema.sql` for the simplified persistence model.
7. Read `docs/portfolio_boundary.md` for what is deliberately excluded from the public edition.

Expected review time: approximately 5–10 minutes for the core evidence path.
