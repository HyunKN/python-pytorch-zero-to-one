import tempfile
from pathlib import Path

import numpy as np
import onnxruntime as ort

from exercise import benchmark_session, build_report, create_demo_model


def main() -> int:
    try:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.onnx"
            create_demo_model(path)
            session = ort.InferenceSession(
                str(path), providers=["CPUExecutionProvider"]
            )
            feed = {session.get_inputs()[0].name: np.ones((1, 4), np.float32)}
            statistics = benchmark_session(session, feed, 2, 10)
            report = build_report(path, session, feed, statistics)
        assert statistics["p90_ms"] >= statistics["median_ms"]
        assert report["model_size_bytes"] > 0
        assert report["provider"] == "CPUExecutionProvider"
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: ONNX Runtime Latency Benchmark")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
