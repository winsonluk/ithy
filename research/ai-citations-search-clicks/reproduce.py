"""Reconcile invented data only. No network, credentials or real analytics."""

import csv
import json
from pathlib import Path


def nonnegative(value):
    number = int(value)
    if number < 0 or str(number) != str(value):
        raise ValueError("expected a nonnegative integer")
    return number


def summarize(directory: Path) -> dict:
    aggregate = json.loads((directory / "aggregate-data.json").read_text())
    if aggregate.get("synthetic") is not True:
        raise ValueError("this exercise requires an explicitly synthetic fixture")
    with (directory / "daily-citations.csv").open(newline="") as f:
        periods = list(csv.DictReader(f))
    with (directory / "language-sample.csv").open(newline="") as f:
        languages = list(csv.DictReader(f))
    documents = aggregate["documents"]
    if not periods or not documents or len({d["id"] for d in documents}) != len(documents):
        raise ValueError("periods and unique documents are required")
    total = nonnegative(aggregate["total_mentions"])
    totals = [sum(nonnegative(r["mentions"]) for r in rows)
              for rows in (periods, languages, documents)]
    if any(value != total for value in totals):
        raise ValueError("mention totals do not reconcile")
    if sum(nonnegative(r["documents"]) for r in languages) != len(documents):
        raise ValueError("language document counts do not reconcile")
    clicks = [nonnegative(d["recorded_clicks"]) for d in documents]
    return {"synthetic": True, "periods": len(periods), "mentions": total,
            "documents": len(documents), "recorded_clicks": sum(clicks),
            "documents_with_recorded_clicks": sum(c > 0 for c in clicks),
            "documents_without_recorded_clicks": sum(c == 0 for c in clicks),
            "mean_daily_mentioned_documents": sum(nonnegative(p["mentioned_documents"])
                                                    for p in periods) / len(periods)}


if __name__ == "__main__":
    print(json.dumps(summarize(Path(__file__).parent), indent=2))
