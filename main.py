"""Print deterministic toy routing and recorded-answer experiments."""

from collections import Counter
from dataclasses import asdict
import json
from pathlib import Path

from moe import EXPERTS, mix
from moa import consensus


def study() -> dict:
    inputs = [-1.75, -1.0, -0.5, 0.0, 0.5, 1.0, 1.75]
    routing = []
    for k in range(1, len(EXPERTS) + 1):
        load = Counter({e.name: 0 for e in EXPERTS})
        rows = []
        for x in inputs:
            result = mix(x, k)
            load.update(result.selected)
            rows.append({"input": x, **asdict(result)})
        routing.append({"k": k, "expert_function_evaluations": sum(load.values()),
                        "selection_load": dict(load), "rows": rows})
    fixture = json.loads((Path(__file__).parent / "examples/agent-answers.json").read_text())
    answers = [{"case": row["case"], "declared_synthetic_truth": row["truth"],
                **asdict(consensus(row["answers"]))} for row in fixture["cases"]]
    return {"synthetic": True, "routing": routing, "recorded_answers": answers,
            "limitations": "No accuracy, speed, model benchmark or service-operation claim."}


if __name__ == "__main__":
    print(json.dumps(study(), indent=2))
