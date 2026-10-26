"""A fixed, synthetic MoE illustration. No learned or production components."""

from dataclasses import dataclass
import math
from typing import Callable


@dataclass(frozen=True)
class Expert:
    name: str
    centre: float
    function: Callable[[float], float]


@dataclass(frozen=True)
class Mixture:
    selected: tuple[str, ...]
    weights: tuple[float, ...]
    output: float


EXPERTS = (
    Expert("linear", -1.0, lambda x: 2.0 * x + 1.0),
    Expert("quadratic", 0.0, lambda x: x * x),
    Expert("sine", 1.0, math.sin),
)


def mix(x: float, k: int = 1, temperature: float = 1.0,
        experts: tuple[Expert, ...] = EXPERTS) -> Mixture:
    """Select nearest centres, then normalize their Gaussian gate weights.

    Stable input-order tie breaking is intentional. Only selected expert
    functions are evaluated. Distances and gate scores still use every centre.
    """
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    if not math.isfinite(temperature) or temperature <= 0:
        raise ValueError("temperature must be positive and finite")
    if not experts or len({e.name for e in experts}) != len(experts):
        raise ValueError("experts must be nonempty with unique names")
    if type(k) is not int or not 1 <= k <= len(experts):
        raise ValueError("k must be an integer within the expert count")
    if any(not math.isfinite(e.centre) for e in experts):
        raise ValueError("centres must be finite")
    scores = [-((x - e.centre) ** 2) / temperature for e in experts]
    if any(not math.isfinite(score) for score in scores):
        raise ValueError("gate scores must be finite; use smaller inputs")
    selected = sorted(range(len(experts)), key=lambda i: (-scores[i], i))[:k]
    peak = scores[selected[0]]
    raw = [math.exp(scores[i] - peak) for i in selected]
    total = math.fsum(raw)
    weights = tuple(value / total for value in raw)
    values = [experts[i].function(x) for i in selected]
    if any(not math.isfinite(value) for value in values):
        raise ValueError("expert outputs must be finite")
    return Mixture(tuple(experts[i].name for i in selected), weights,
                   math.fsum(w * value for w, value in zip(weights, values)))
