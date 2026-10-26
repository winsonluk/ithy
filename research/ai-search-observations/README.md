# Crawler counting — synthetic teaching appendix

**These are invented teaching records, not anonymized service logs.** The generic agent labels, counts and evidence checks have no mapping to a real crawler, IP range, publisher, capture window, infrastructure or account. No production provenance hashes or export files are included.

```sh
python research/ai-search-observations/summarize.py
```

The script checks nonnegative integer counts, verifies that matched checks cannot exceed requests, and reports totals from `synthetic-observations.csv`. The artificial fixture has 48 requests and 40 matched checks. An evidence check is merely a counting field in this exercise; the program performs no network identity verification.

Even in a real, properly instrumented study, a crawler request would not establish a citation, a human visit, a unique person, a purchase or a ranking effect. Self-reported agent labels alone would not establish identity. A defensible empirical study would separately document collection scope, identification uncertainty, deduplication and retention without disclosing private logs.

Earlier publisher-specific observations are no longer distributed here. This appendix preserves a general methods lesson; it cannot reproduce an earlier case study's empirical totals.
