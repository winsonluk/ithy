# Ithy — a small mixture-of-experts study

How does selecting a few experts change a mixture's output? What happens when several agents agree for the wrong reason? This repository explores those questions through small, runnable examples.

The examples are educational and self-contained. They use mathematical functions and invented answer records, require only Python's standard library, and make no network requests. They do not implement the hosted Ithy service or disclose its models, prompts, search configuration, publishing system or operations.

## Start here

Requires Python 3.10 or later. No account, credentials, package installation or paid inference is needed.

```sh
python main.py
python -m unittest discover -s tests -v
```

`main.py` prints a reproducible comparison of top-1, top-2 and dense routing over the same inputs. It reports the selected experts, mixture outputs, routing load and number of expert-function evaluations. That count is an operation count for this toy, not a measured speedup or an LLM cost estimate.

## Two ideas that need different names

| Idea | Where the experts live | What this repository demonstrates |
| --- | --- | --- |
| Neural mixture of experts (MoE) | Subnetworks inside a model; a gate chooses their contribution | A fixed distance-based gate over three mathematical functions, with top-k selection and renormalization |
| Mixture of agents (MoA) | Separate model or agent responses combined at the application level | Aggregation of recorded synthetic answers, including a tie, abstention and correlated error |

The routing example has no learned parameters, neural layers, training, capacity constraints or distributed execution. The answer example calls no language models. Neither reproduces a paper's benchmark or demonstrates how a commercial service works.

## Study map

- [Routing and aggregation notes](docs/study.md): equations, assumptions, experiments and failure cases.
- [`moe.py`](moe.py): stable softmax, deterministic top-k selection and weighted output.
- [`moa.py`](moa.py): a deliberately limited consensus baseline that keeps disagreement visible.
- [Recorded agent fixture](examples/agent-answers.json): invented responses with declared synthetic ground truth.
- [Citation versus click methods](research/ai-citations-search-clicks): a synthetic arithmetic exercise.
- [Crawler observation methods](research/ai-search-observations): a separate synthetic counting exercise.

The measurement appendices illustrate why mentions, crawler requests and clicks are different observations. Their data are invented, not anonymized production extracts, and cannot reproduce any publisher's previously reported figures.

## Reading

- Shazeer et al. (2017), [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538).
- Fedus, Zoph and Shazeer (2021; revised 2022), [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961).
- Wang et al. (2024), [Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692), and the authors' [MoA reference implementation](https://github.com/togethercomputer/MoA).

These papers motivate the questions; this project does not claim their results.

## Scope and contributions

Keep contributions focused on general routing, aggregation, evaluation and reproducibility. Use synthetic or explicitly licensed public fixtures. Do not contribute service configuration, real analytics, customer material, credentials or production prompts. See [CONTRIBUTING.md](CONTRIBUTING.md).

An educational project maintained by [Ithy](https://ithy.com). MIT licensed; see [LICENSE](LICENSE). [繁體中文](README-CN.md).
