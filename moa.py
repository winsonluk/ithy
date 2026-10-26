"""A consensus baseline over invented answer records, not an LLM evaluator."""

from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Consensus:
    answer: str | None
    support: int
    answered: int
    abstained: int
    disagreement: bool


def consensus(answers: list[str | None]) -> Consensus:
    """Require a strict majority of non-abstaining, normalized strings.

    Case and surrounding/repeated whitespace are ignored. Semantic equivalence,
    evidence quality, agent independence and factual truth are not evaluated.
    """
    normalized = [" ".join(a.casefold().split()) for a in answers if a is not None]
    normalized = [a for a in normalized if a]
    counts = Counter(normalized)
    if not counts:
        return Consensus(None, 0, 0, len(answers), False)
    leader, count = counts.most_common(1)[0]
    answer = leader if count > len(normalized) / 2 else None
    return Consensus(answer, count, len(normalized), len(answers) - len(normalized),
                     len(counts) > 1)
