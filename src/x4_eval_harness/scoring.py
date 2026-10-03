"""X4 evidence scoring."""
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import List


class Verdict(str, Enum):
    VALIDATED = "VALIDATED"
    UNKNOWN = "UNKNOWN"
    FAIL = "FAIL"


@dataclass
class EvidenceItem:
    source: str
    claim: str
    observed: bool


def score(items: List[EvidenceItem]) -> Verdict:
    if not items:
        return Verdict.UNKNOWN
    if all(i.observed for i in items):
        return Verdict.VALIDATED
    if any(i.observed for i in items):
        return Verdict.UNKNOWN
    return Verdict.FAIL
