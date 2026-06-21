from pathlib import Path
from time import perf_counter

import numpy as np
import onnxruntime as ort
import torch
from torch import nn


def create_demo_model(output_path: Path) -> None:
    """Benchmark가 독립 실행되도록 작은 ONNX 모델을 생성합니다."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    torch.manual_seed(0)
    model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 3)).eval()
    sample = torch.ones(1, 4)
    torch.onnx.export(
        model,
        sample,
        str(output_path),
        opset_version=18,
        input_names=["input"],
        output_names=["output"],
    )


def benchmark_session(
    session: ort.InferenceSession,
    input_feed: dict[str, np.ndarray],
    warmup_runs: int,
    measured_runs: int,
) -> dict[str, float]:
    """Warm-up을 제외한 ONNX Runtime latency 통계를 millisecond로 반환합니다."""
    if warmup_runs < 0 or measured_runs <= 0:
        raise ValueError("warmup_runs는 0 이상, measured_runs는 1 이상이어야 합니다.")

    for _ in range(warmup_runs):
        session.run(None, input_feed)

    latencies_ms: list[float] = []
    for _ in range(measured_runs):
        started = perf_counter()
        session.run(None, input_feed)
        latencies_ms.append((perf_counter() - started) * 1000)

    values = np.asarray(latencies_ms, dtype=np.float64)
    return {
        "median_ms": float(np.median(values)),
        "p90_ms": float(np.percentile(values, 90)),
        "min_ms": float(values.min()),
        "max_ms": float(values.max()),
    }


def build_report(
    model_path: Path,
    session: ort.InferenceSession,
    input_feed: dict[str, np.ndarray],
    statistics: dict[str, float],
) -> dict[str, object]:
    """재현에 필요한 runtime, provider, input shape와 model size를 기록합니다."""
    return {
        "onnxruntime_version": ort.__version__,
        "provider": session.get_providers()[0],
        "input_shapes": {name: list(value.shape) for name, value in input_feed.items()},
        "model_size_bytes": model_path.stat().st_size,
        **statistics,
    }


def main() -> None:
    model_path = Path("artifacts/benchmark_model.onnx")
    create_demo_model(model_path)
    session = ort.InferenceSession(
        str(model_path), providers=["CPUExecutionProvider"]
    )
    input_feed = {session.get_inputs()[0].name: np.ones((1, 4), dtype=np.float32)}
    statistics = benchmark_session(
        session, input_feed, warmup_runs=10, measured_runs=100
    )
    report = build_report(model_path, session, input_feed, statistics)

    print("Benchmark report")
    for key, value in report.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
