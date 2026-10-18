# x4-eval-harness

**Evidence-first evaluation harness for AI agents.**

Claim graphs, source ranking, verification loops, and the canonical X4 scoring path:

```
OBSERVED → CORRELATED → HYPOTHESIS → VALIDATED / UNKNOWN
```

No PASS without evidence.

<!-- X4-APEX-DIAGRAM-START:x4-eval-harness -->

```mermaid
flowchart LR
    SUITE[Evaluation Suite] --> LINEAGE[Validate Dataset and Run Lineage]
    LINEAGE -->|missing| BLOCK[Reject Unverifiable Run]
    LINEAGE -->|valid| EXEC[Run Agent or Candidate]
    EXEC --> OUTPUT[Capture Output and Evidence]
    OUTPUT --> SCORE[Score Against Expected Behavior]
    SCORE --> BASELINE[Compare with Baseline]
    BASELINE -->|within threshold| ACCEPT[Accept with Report]
    BASELINE -->|regression| FAIL[Fail Quality Gate]
    OUTPUT --> STATES[OBSERVED / CORRELATED / HYPOTHESIS / VALIDATED / UNKNOWN]
    STATES --> REPORT[Publish Reproducible Evaluation Record]
```

<!-- X4-APEX-DIAGRAM-END:x4-eval-harness -->

## Quick Start

```bash
pip install -e ".[dev]"
python -m x4_eval_harness.run --suite examples/basic.json
```

## License

Apache-2.0
