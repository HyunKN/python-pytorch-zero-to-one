import importlib.util
from pathlib import Path
from types import ModuleType


REPOSITORY_ROOT = Path(__file__).parents[1]


def load_module(relative_path: str, module_name: str) -> ModuleType:
    """하이픈이 포함된 실습 경로의 Python module을 불러옵니다."""
    path = REPOSITORY_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Module을 불러올 수 없습니다: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
