import json
import tempfile
import unittest
from pathlib import Path

import numpy as np

from module_loader import load_module


class PythonDemoTests(unittest.TestCase):
    def test_prediction_score_analyzer(self):
        module = load_module(
            "01-python/01-prediction-score-analyzer/demo.py", "score_demo"
        )
        result = module.analyze_scores(
            ["cat", "dog", "bird", "rabbit"],
            [0.12, 0.71, 0.10, 0.07],
            threshold=0.50,
        )

        self.assertEqual(result["top1"], {"label": "dog", "score": 0.71})
        self.assertEqual(
            [item["label"] for item in result["top3"]], ["dog", "cat", "bird"]
        )
        self.assertEqual(result["decision"], "dog")

        unknown = module.analyze_scores(["cat", "dog"], [0.2, 0.3], 0.5)
        self.assertEqual(unknown["decision"], "unknown")

    def test_list_dictionary_summary(self):
        module = load_module(
            "01-python/02-list-dictionary-summary/demo.py", "summary_demo"
        )
        products = [
            {"name": "notebook", "price": 3500, "stock": 4},
            {"name": "pen", "price": 1200, "stock": 12},
            {"name": "mug", "price": 9000, "stock": 2},
        ]

        result = module.summarize_products(products, low_stock_threshold=3)

        self.assertEqual(result["total_stock"], 18)
        self.assertEqual(result["most_expensive"], "mug")
        self.assertEqual(result["low_stock"], ["mug"])

    def test_json_reader(self):
        module = load_module("01-python/03-json-data-reader/demo.py", "json_demo")
        records = [
            {"name": "apple", "category": "fruit"},
            {"name": "carrot", "category": "vegetable"},
            {"name": "banana", "category": "fruit"},
        ]

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.json"
            path.write_text(json.dumps(records), encoding="utf-8")
            loaded = module.load_records(path)

        self.assertEqual(loaded, records)
        self.assertEqual(
            module.count_categories(loaded), {"fruit": 2, "vegetable": 1}
        )

    def test_image_folder_inspector(self):
        module = load_module(
            "01-python/04-image-folder-inspector/demo.py", "folder_demo"
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "cat.JPG").touch()
            (root / "dog.png").touch()
            (root / "nested" / "bird.jpeg").touch()
            (root / "notes.txt").touch()
            result = module.inspect_image_folder(root)

        self.assertEqual(result["total"], 3)
        self.assertEqual(result["by_extension"], {".jpeg": 1, ".jpg": 1, ".png": 1})


class NumPyDemoTests(unittest.TestCase):
    def test_array_summary(self):
        module = load_module("02-numpy/01-array-and-shape/demo.py", "array_demo")
        result = module.summarize_array(np.array([[1, 2, 3], [4, 5, 6]]))

        self.assertEqual(result["shape"], (2, 3))
        self.assertEqual(result["ndim"], 2)
        self.assertEqual(result["minimum"], 1.0)
        self.assertEqual(result["maximum"], 6.0)
        self.assertEqual(result["mean"], 3.5)

    def test_image_normalization(self):
        module = load_module(
            "02-numpy/02-image-normalization/demo.py", "normalization_demo"
        )
        image = np.array([[[0, 127, 255]]], dtype=np.uint8)
        mean = np.array([0.5, 0.5, 0.5], dtype=np.float32)
        std = np.array([0.5, 0.5, 0.5], dtype=np.float32)

        result = module.normalize_image(image, mean, std)

        self.assertEqual(result.dtype, np.float32)
        self.assertEqual(result.shape, image.shape)
        np.testing.assert_allclose(
            result,
            np.array([[[-1.0, -0.00392157, 1.0]]], dtype=np.float32),
            atol=1e-6,
        )
        np.testing.assert_array_equal(image, np.array([[[0, 127, 255]]], dtype=np.uint8))

    def test_cosine_top_k(self):
        module = load_module(
            "02-numpy/03-cosine-similarity-topk/demo.py", "cosine_demo"
        )
        embeddings = np.array(
            [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=np.float32
        )
        query = np.array([1.0, 0.0], dtype=np.float32)

        indices, scores = module.cosine_top_k(embeddings, query, k=2)

        np.testing.assert_array_equal(indices, np.array([0, 2]))
        np.testing.assert_allclose(scores, np.array([1.0, 2**-0.5]), atol=1e-6)


if __name__ == "__main__":
    unittest.main()
