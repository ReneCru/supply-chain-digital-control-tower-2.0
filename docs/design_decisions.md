# Key Design Decisions

## Deterministic KPI core
OTD calculation is deterministic because operational metrics used for control and audit should be reproducible from the same evidence.

## Recommendation is not authorization
A recommendation object can propose a next step but cannot authorize itself. A separate human decision is required before the workflow reports an action as ready.

## Synthetic public data
The public repository uses synthetic identifiers and observations so the technical design can be reviewed without exposing employer, customer, supplier, or transactional information.

## Simplified public risk logic
Risk thresholds in the Portfolio Edition are illustrative. They demonstrate the implementation pattern but are intentionally not the complete private policy/intelligence model.

## Outcome measurement without causal overclaim
The workflow can report before/after KPI change while explicitly avoiding an unsupported claim that an intervention caused the change.

## Small public vertical slice
The recruiter edition favors a small end-to-end path that can be understood and tested quickly rather than publishing the full private platform.
