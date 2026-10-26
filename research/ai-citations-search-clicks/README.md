# Citation and click arithmetic — synthetic teaching appendix

**All data in this directory are invented.** They are not anonymized, rescaled or encoded production observations. They contain no real publisher, dates, article paths, account exports or export fingerprints. They cannot reproduce any publisher's historical results.

This peripheral methods exercise illustrates a measurement problem that also matters when evaluating agent systems: a reported mention, a page receiving a click, and a human reader are different units. Adding their counts or treating one as a proxy for another can produce a misleading conclusion.

Run from the repository root:

```sh
python research/ai-citations-search-clicks/reproduce.py
```

The script reconciles eight artificial periods, eight artificial documents and three artificial language groups. It checks that daily and language citation totals match the fixture and counts documents with and without recorded clicks. A document without a recorded click is not proof that no person read it: this fixture says nothing about instrumentation completeness, attribution windows or other sources.

`aggregate-data.json`, `daily-citations.csv` and `language-sample.csv` are transparent toy inputs. Numbers were chosen independently for arithmetic examples, not derived from a service's logs. The script verifies consistency, not authenticity or causality. Earlier publisher-specific companion material is no longer distributed here; do not cite these fixtures as empirical observations.
