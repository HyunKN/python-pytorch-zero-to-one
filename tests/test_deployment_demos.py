import tempfile
import unittest
from pathlib import Path

import numpy as np
import onnx
import onnxruntime as ort
import torch
from torch import nn

from module_loader import load_module


class DeploymentDemoTests(unittest.TestCase):
    def test_onnx_export_inference_and_parity(self):
        module = load_module(
            "04-deployment/01-onnx-export-parity/demo.py", "onnx_export_demo"
        )
        torch.manual_seed(0)
        model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 3)).eval()
        sample = torch.randn(2, 4)

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.onnx"
            module.export_to_onnx(model, sample, path)
            onnx.checker.check_model(onnx.load(path))

            with torch.no_grad():
                pytorch_output = model(sample).numpy()
            onnx_output = module.run_onnx(path, sample.numpy())

        comparison = module.compare_outputs(pytorch_output, onnx_output)
        self.assertTrue(comparison["parity"])
        self.assertLess(comparison["max_absolute_difference"], 1e-5)
        self.assertGreater(comparison["cosine_similarity"], 0.9999)

    def test_output_comparison_handles_zero_vectors(self):
        module = load_module(
            "04-deployment/01-onnx-export-parity/demo.py", "onnx_zero_demo"
        )
        zeros = np.zeros((1, 3), dtype=np.float32)
        nonzero = np.ones((1, 3), dtype=np.float32)

        same = module.compare_outputs(zeros, zeros)
        different = module.compare_outputs(zeros, nonzero)

        self.assertTrue(same["parity"])
        self.assertEqual(same["cosine_similarity"], 1.0)
        self.assertFalse(different["parity"])
        self.assertEqual(different["cosine_similarity"], 0.0)

    def test_latency_benchmark_and_report(self):
        module = load_module(
            "04-deployment/02-onnxruntime-latency-benchmark/demo.py",
            "latency_demo",
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.onnx"
            module.create_demo_model(path)
            session = ort.InferenceSession(
                str(path), providers=["CPUExecutionProvider"]
            )
            input_feed = {session.get_inputs()[0].name: np.ones((1, 4), np.float32)}
            statistics = module.benchmark_session(
                session, input_feed, warmup_runs=2, measured_runs=10
            )
            report = module.build_report(path, session, input_feed, statistics)

        self.assertEqual(set(statistics), {"median_ms", "p90_ms", "min_ms", "max_ms"})
        self.assertGreaterEqual(statistics["min_ms"], 0)
        self.assertGreaterEqual(statistics["p90_ms"], statistics["median_ms"])
        self.assertEqual(report["provider"], "CPUExecutionProvider")
        self.assertEqual(report["input_shapes"], {"input": [1, 4]})
        self.assertGreater(report["model_size_bytes"], 0)


if __name__ == "__main__":
    unittest.main()
