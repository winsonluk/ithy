# Routing, aggregation and the questions they leave open

## Fixed gate experiment

For an input `x` and expert centre `c_i`, the toy gate score is

```text
s_i = -(x - c_i)^2 / temperature
S = indices of the k largest scores
w_i = exp(s_i - max_selected_score) / sum_selected exp(s_j - max_selected_score)
y = sum_selected w_i * expert_i(x)
```

The experts are a linear function, a quadratic function and sine. Their centres, functions and inputs were chosen for illustration. They have no relationship to a deployed product. The gate is fixed, so this is an illustration of selection and normalization, not a trained sparse neural network.

With seven inputs, top-1 evaluates seven expert functions; top-2 evaluates fourteen; dense routing evaluates twenty-one. Every mode still scores all three centres. Dispatch, memory, communication, training and language-model token costs are absent. Fewer function evaluations must not be reported as an equivalent real-world speedup.

At equal distances, input order breaks ties. Near a boundary, top-1 can change abruptly; top-2 blends the selected values but can still change when its selected set changes. Larger temperature makes selected weights more even. It does not change the ordering of this gate's finite distance scores.

There is no natural ground-truth output for this invented mixture. The program reports outputs and load, not a quality leaderboard. Choosing a target defined by the same gate would make an apparent accuracy result circular.

Useful exercises:

1. Change the temperature and inspect weights near `x = 0.5`.
2. Add inputs concentrated near one centre and inspect selection imbalance.
3. Replace one expert with an extreme output and observe how routing affects the mixture.
4. Compare top-k with dense output while accounting separately for gate and expert work.

## Recorded-answer experiment

`moa.py` counts normalized strings and returns an answer only if a strict majority of non-abstaining records agrees. It preserves answered/abstained counts and a disagreement flag. An answer with one vote out of one non-abstention is possible; support is not confidence.

The fixture contains a deliberately unanimous wrong answer. This shows why consensus alone cannot establish truth. Repeated agents may share training data, sources or assumptions, and string equality cannot evaluate those dependencies. Different wording can also cause a false disagreement.

This baseline is not the layered model synthesis in the [MoA paper](https://arxiv.org/abs/2406.04692). No model is called and no prompt template is supplied. A serious follow-up would need a declared task distribution, independently established labels, contamination controls, equal-budget baselines, uncertainty estimates and failure analysis. More agents alone is not evidence of improvement.

## Terminology and attribution

The [2017 sparse MoE paper](https://arxiv.org/abs/1701.06538) describes a trainable gate selecting feed-forward subnetworks. [Switch Transformers](https://arxiv.org/abs/2101.03961) studies sparse routing within neural models. The [2024 MoA paper](https://arxiv.org/abs/2406.04692) combines responses across layers of language-model agents. These operate at different levels; avoid treating the names as interchangeable.

The implementation here is a small independent teaching example, not a reproduction of any of those systems, their evaluation scores, or the Ithy application.
