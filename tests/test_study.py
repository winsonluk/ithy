from importlib.util import module_from_spec, spec_from_file_location
import json
import math
from pathlib import Path
import shutil
import socket
import tempfile
import unittest
from unittest.mock import patch

from main import study
from moe import Expert, mix
from moa import consensus


ROOT = Path(__file__).resolve().parents[1]


def load(relative):
    spec = spec_from_file_location("appendix", ROOT / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RoutingTests(unittest.TestCase):
    def test_only_selected_experts_execute(self):
        calls = []
        experts = tuple(Expert(str(i), float(i), lambda x, i=i: calls.append(i) or i)
                        for i in range(3))
        result = mix(1.1, 1, experts=experts)
        self.assertEqual(calls, [1])
        self.assertEqual(result.weights, (1.0,))
        self.assertEqual(result.output, 1.0)

    def test_ties_are_deterministic(self):
        self.assertEqual(mix(0.5, 1).selected, ("quadratic",))

    def test_dense_weighted_output(self):
        result = mix(0.0, 3)
        denominator = 1.0 + 2.0 / math.e
        self.assertAlmostEqual(sum(result.weights), 1.0)
        self.assertAlmostEqual(result.output, (1.0 / math.e) / denominator)

    def test_tiny_temperature_is_stable(self):
        result = mix(0.1, 3, 1e-100)
        self.assertEqual(result.weights, (1.0, 0.0, 0.0))

    def test_invalid_gates_fail(self):
        for kwargs in ({"k": 0}, {"k": 4}, {"k": True}, {"temperature": 0},
                       {"temperature": float("nan")}, {"experts": ()}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                mix(0.0, **kwargs)
        with self.assertRaises(ValueError):
            mix(float("inf"))

    def test_operation_counts_and_offline_execution(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            result = study()
        self.assertEqual([r["expert_function_evaluations"] for r in result["routing"]],
                         [7, 14, 21])


class AggregationTests(unittest.TestCase):
    def test_normalization_and_abstentions(self):
        result = consensus([" Four ", "FOUR", None, ""])
        self.assertEqual((result.answer, result.support, result.answered, result.abstained),
                         ("four", 2, 2, 2))

    def test_tie_does_not_invent_consensus(self):
        result = consensus(["a", "b", None])
        self.assertIsNone(result.answer)
        self.assertTrue(result.disagreement)

    def test_all_abstain(self):
        result = consensus([None, " "])
        self.assertIsNone(result.answer)
        self.assertEqual(result.abstained, 2)

    def test_unanimity_can_be_wrong(self):
        case = next(r for r in study()["recorded_answers"] if r["case"] == "correlated_error")
        self.assertNotEqual(case["answer"], case["declared_synthetic_truth"])
        self.assertFalse(case["disagreement"])


class AppendixTests(unittest.TestCase):
    def test_citation_reconciliation_and_mutation_rejection(self):
        module = load("research/ai-citations-search-clicks/reproduce.py")
        source = ROOT / "research/ai-citations-search-clicks"
        self.assertEqual(module.summarize(source)["mentions"], 128)
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "fixture"
            shutil.copytree(source, target)
            p = target / "aggregate-data.json"
            data = json.loads(p.read_text())
            data["total_mentions"] += 1
            p.write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                module.summarize(target)

    def test_crawler_reconciliation_and_impossible_checks(self):
        module = load("research/ai-search-observations/summarize.py")
        path = ROOT / "research/ai-search-observations/synthetic-observations.csv"
        self.assertEqual(module.summarize(path)["matched_checks"], 40)
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "fixture.csv"
            p.write_text("synthetic_agent,requests,matched_checks\nexample,1,2\n")
            with self.assertRaises(ValueError):
                module.summarize(p)


if __name__ == "__main__":
    unittest.main()
