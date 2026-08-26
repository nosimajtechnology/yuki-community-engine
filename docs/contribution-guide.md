# Contribution guide

This repository is private. Do not publish, license, release, or announce changes externally without explicit approval.

## Contribution types

- **Canon:** requires Tier 1/2 evidence, source-register update, conflict review, and explicit approval.
- **World research:** include date, source, supported claim, and historical-vs-interpretive label.
- **Workflow:** show which mode or failure it improves and preserve existing approval gates.
- **Adapter:** verify current provider constraints and keep creative intent unchanged.
- **Example/remix:** label invented material and keep rights/attribution clear.

## Review checklist

- Does the change preserve the bundled turnaround as absolute authority?
- Are official claims, community convention, and interpretation separated?
- Does any new shot continue the prior approved state?
- Does the change add avoidable complexity or duplicate instructions?
- Is provider-specific logic isolated under `adapters/`?
- Does `python3 scripts/validate_engine.py` pass?
- Were affected dry-runs updated?

Do not add a public open-source license without owner approval.

