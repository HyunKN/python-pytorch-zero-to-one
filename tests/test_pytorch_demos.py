import tempfile
import unittest
from pathlib import Path

import torch
from PIL import Image
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import transforms

from module_loader import load_module


class TensorAndAutogradDemoTests(unittest.TestCase):
    def test_tensor_summary_and_matrix_product(self):
        module = load_module("03-pytorch/01-tensor-basics/demo.py", "tensor_demo")
        tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

        summary = module.summarize_tensor(tensor)
        product = module.matrix_product(tensor, torch.eye(2))

        self.assertEqual(summary["shape"], (2, 2))
        self.assertEqual(summary["dtype"], "torch.float32")
        self.assertEqual(summary["mean"], 2.5)
        torch.testing.assert_close(product, tensor)

    def test_linear_regression_loss_decreases(self):
        module = load_module(
            "03-pytorch/02-autograd-linear-regression/demo.py", "regression_demo"
        )
        torch.manual_seed(0)
        inputs = torch.linspace(-1, 1, 40).unsqueeze(1)
        targets = 3 * inputs + 2

        model, losses = module.train_linear_regression(
            inputs, targets, epochs=120, learning_rate=0.1
        )

        self.assertLess(losses[-1], losses[0] * 0.01)
        prediction = model(torch.tensor([[2.0]])).item()
        self.assertAlmostEqual(prediction, 8.0, delta=0.2)


class VisionPipelineDemoTests(unittest.TestCase):
    def test_fashion_mlp_training_and_checkpoint(self):
        module = load_module(
            "03-pytorch/03-fashion-mnist-mlp/demo.py", "fashion_mlp_demo"
        )
        torch.manual_seed(0)
        model = module.FashionMLP()
        loader = module.build_synthetic_loader(sample_count=32, batch_size=8)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        criterion = nn.CrossEntropyLoss()

        loss = module.train_one_epoch(
            model, loader, criterion, optimizer, torch.device("cpu")
        )
        accuracy = module.evaluate(model, loader, torch.device("cpu"))

        self.assertGreater(loss, 0)
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)
        self.assertEqual(model(torch.randn(2, 1, 28, 28)).shape, (2, 10))

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.pt"
            module.save_checkpoint(model, path)
            restored = module.FashionMLP()
            module.load_checkpoint(restored, path, torch.device("cpu"))
            for expected, actual in zip(
                model.parameters(), restored.parameters(), strict=True
            ):
                torch.testing.assert_close(actual, expected)

    def test_fashion_cnn_forward_and_training(self):
        module = load_module(
            "03-pytorch/04-fashion-mnist-cnn/demo.py", "fashion_cnn_demo"
        )
        torch.manual_seed(0)
        model = module.FashionCNN()
        loader = module.build_synthetic_loader(sample_count=16, batch_size=8)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

        loss = module.train_one_epoch(
            model,
            loader,
            nn.CrossEntropyLoss(),
            optimizer,
            torch.device("cpu"),
        )

        self.assertGreater(loss, 0)
        self.assertEqual(model(torch.randn(2, 1, 28, 28)).shape, (2, 10))
        self.assertGreater(module.count_parameters(model), 0)

    def test_custom_dataset_reads_rgb_tensors(self):
        module = load_module(
            "03-pytorch/05-custom-dataset-dataloader/demo.py", "dataset_demo"
        )
        transform = transforms.ToTensor()

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first.png"
            second = root / "second.png"
            Image.new("RGB", (8, 8), color="red").save(first)
            Image.new("RGB", (8, 8), color="blue").save(second)
            dataset = module.ImageClassificationDataset(
                [(first, 0), (second, 1)], transform=transform
            )
            image, label = dataset[0]

        self.assertEqual(len(dataset), 2)
        self.assertEqual(image.shape, (3, 8, 8))
        self.assertEqual(label, 0)

    def test_resnet_classifier_and_freezing(self):
        module = load_module(
            "03-pytorch/06-resnet-finetuning/demo.py", "resnet_demo"
        )
        model = module.build_resnet(
            num_classes=3, freeze_backbone=True, pretrained=False
        )

        self.assertEqual(model.fc.out_features, 3)
        self.assertTrue(model.fc.weight.requires_grad)
        self.assertFalse(model.conv1.weight.requires_grad)
        self.assertEqual(model(torch.randn(1, 3, 64, 64)).shape, (1, 3))
        self.assertEqual(
            set(module.trainable_parameters(model)),
            {parameter for parameter in model.parameters() if parameter.requires_grad},
        )

    def test_evaluation_and_error_collection(self):
        module = load_module(
            "03-pytorch/07-evaluation-error-analysis/demo.py", "evaluation_demo"
        )
        logits = torch.tensor(
            [[4.0, 1.0], [1.0, 4.0], [3.0, 2.0], [1.0, 5.0]]
        )
        labels = torch.tensor([0, 1, 1, 1])
        loader = DataLoader(TensorDataset(logits, labels), batch_size=2)

        metrics = module.evaluate_classifier(
            nn.Identity(), loader, torch.device("cpu"), num_classes=2
        )
        mistakes = module.collect_misclassified(
            nn.Identity(), loader, torch.device("cpu")
        )

        self.assertEqual(metrics["accuracy"], 0.75)
        torch.testing.assert_close(
            metrics["confusion_matrix"], torch.tensor([[1, 0], [1, 2]])
        )
        torch.testing.assert_close(
            metrics["class_recall"], torch.tensor([1.0, 2 / 3])
        )
        self.assertEqual(len(mistakes), 1)
        self.assertEqual(mistakes[0]["true_label"], 1)
        self.assertEqual(mistakes[0]["predicted_label"], 0)


if __name__ == "__main__":
    unittest.main()
