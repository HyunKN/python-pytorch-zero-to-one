from time import perf_counter

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
