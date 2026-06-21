from time import perf_counter
from pathlib import Path

import numpy as np
import onnxruntime as ort


def benchmark_session(
    session: ort.InferenceSession,
    input_feed: dict[str, np.ndarray],
    warmup_runs: int,
    measured_runs: int,
) -> dict[str, float]:
    """ONNX Runtime latency 통계를 millisecond 단위로 반환합니다."""
    raise NotImplementedError("Latency benchmark를 구현하세요.")


def create_demo_model(output_path: Path) -> None:
    raise NotImplementedError("Benchmark용 ONNX 모델 생성을 구현하세요.")


def build_report(
    model_path: Path,
    session: ort.InferenceSession,
    input_feed: dict[str, np.ndarray],
    statistics: dict[str, float],
) -> dict[str, object]:
    raise NotImplementedError("Benchmark report 생성을 구현하세요.")
