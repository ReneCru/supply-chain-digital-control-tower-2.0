# Security & Disclosure Boundary

This repository is a deliberately sanitized portfolio edition.

## Data policy

Only synthetic demonstration data may be committed. Real employer, supplier, customer, ERP, purchase-order, contract, credential, email, part-number, or confidential operational data is prohibited.

## Secrets

Credentials and local environment files must never be committed. `.env` files, private keys, local databases, raw data, and processed local data are excluded through `.gitignore`.

## Intellectual-property boundary

This repository intentionally excludes private implementation details such as proprietary policy thresholds, complete scenario intelligence, advanced recommendation logic, remediation playbooks, predictive intelligence, AI-copilot internals, and private decision-replay mechanisms.

## Human authority

The demonstrated system is decision support. It does not autonomously authorize material operational actions.

## Reporting

If a credential, confidential datum, or other sensitive artifact is discovered, remove public exposure immediately and rotate/revoke affected credentials where applicable. Git history must also be reviewed because deleting a file from the latest tree alone does not remove it from prior commits.
