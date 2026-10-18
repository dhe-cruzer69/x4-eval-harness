# x4-eval-harness

**Evidence-first evaluation harness for AI agents.**

Claim graphs, source ranking, verification loops, and the canonical X4 scoring path:

```
OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED / UNKNOWN
```

No PASS without evidence.

## Quick Start

```bash
pip install -e ".[dev]"
python -m x4_eval_harness.run --suite examples/basic.json
```

## License

Apache-2.0

## APEX Architecture Map

> Status: architecture documentation; implementation and deployment claims require independent verification.

```mermaid
flowchart TB
  Corpus[(Versioned evaluation corpus)] --> Provenance[Validate case provenance]
  Provenance -->|missing metadata| Reject[Reject evaluation run]
  Provenance -->|complete| Runner[Run cases in pinned environment]
  Runner --> Raw[Capture raw outputs and errors]
  Raw --> Scorer[Compute metric set]
  Scorer --> Baseline[Load signed or versioned baseline]
  Baseline --> Compare[Compare per-metric deltas]
  Scorer --> Compare
  Compare --> Threshold{Regression policy satisfied?}
  Threshold -->|no| Block[Fail CI + attach evidence]
  Threshold -->|yes| Report[Generate report + artifacts]
  Report --> Review[Human review for material changes]
  Review --> Release[Eligible for downstream release gate]
```
**Evidence note:** Corpus versioning, deterministic execution, metric definitions, and regression thresholds need to be confirmed from source and CI configuration.

