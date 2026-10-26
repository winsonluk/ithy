"""Summarize an invented crawler-counting fixture, without network access."""

import csv
import json
from pathlib import Path


def summarize(path: Path) -> dict:
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    labels = set()
    requests = matched = 0
    for row in rows:
        label = row["synthetic_agent"]
        count, checks = int(row["requests"]), int(row["matched_checks"])
        if not label or label in labels or not 0 <= checks <= count:
            raise ValueError("expected unique labels and 0 <= checks <= requests")
        labels.add(label)
        requests += count
        matched += checks
    if not rows:
        raise ValueError("fixture cannot be empty")
    return {"synthetic": True, "agent_groups": len(rows), "requests": requests,
            "matched_checks": matched, "unmatched_checks": requests - matched}


if __name__ == "__main__":
    print(json.dumps(summarize(Path(__file__).with_name("synthetic-observations.csv")), indent=2))
