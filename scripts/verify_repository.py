import ast
import py_compile
import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
STAGES = [
    "01-python/01-prediction-score-analyzer",
    "01-python/02-list-dictionary-summary",
    "01-python/03-json-data-reader",
    "01-python/04-image-folder-inspector",
    "02-numpy/01-array-and-shape",
    "02-numpy/02-image-normalization",
    "02-numpy/03-cosine-similarity-topk",
    "03-pytorch/01-tensor-basics",
    "03-pytorch/02-autograd-linear-regression",
    "03-pytorch/03-fashion-mnist-mlp",
    "03-pytorch/04-fashion-mnist-cnn",
    "03-pytorch/05-custom-dataset-dataloader",
    "03-pytorch/06-resnet-finetuning",
    "03-pytorch/07-evaluation-error-analysis",
    "04-deployment/01-onnx-export-parity",
    "04-deployment/02-onnxruntime-latency-benchmark",
]
REQUIRED_STAGE_FILES = {"README.md", "demo.py", "exercise.py", "check.py", "notes.md"}


def local_markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    return [
        target.split("#", 1)[0]
        for target in targets
        if not target.startswith(("http://", "https://", "#"))
    ]


def public_definitions(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }


def exercise_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "exercise":
            names.update(alias.name for alias in node.names)
    return names


def main() -> int:
    errors: list[str] = []

    for relative in STAGES:
        stage = ROOT / relative
        if not stage.is_dir():
            errors.append(f"단계 폴더 누락: {relative}")
            continue

        missing = REQUIRED_STAGE_FILES - {path.name for path in stage.iterdir()}
        if missing:
            errors.append(f"{relative} 필수 파일 누락: {sorted(missing)}")

        readme = stage / "README.md"
        if readme.exists():
            text = readme.read_text(encoding="utf-8")
            for required_name in ["demo.py", "exercise.py", "check.py", "notes.md"]:
                if required_name not in text:
                    errors.append(f"{relative}/README.md 안내 누락: {required_name}")

        check = stage / "check.py"
        exercise = stage / "exercise.py"
        if check.exists() and exercise.exists():
            missing_api = exercise_imports(check) - public_definitions(exercise)
            if missing_api:
                errors.append(f"{relative} exercise API 누락: {sorted(missing_api)}")

    for markdown in ROOT.rglob("*.md"):
        if ".venv" in markdown.parts:
            continue
        for target in local_markdown_links(markdown):
            if not (markdown.parent / target).resolve().exists():
                errors.append(f"깨진 link: {markdown.relative_to(ROOT)} -> {target}")

    for python_file in ROOT.rglob("*.py"):
        if ".venv" in python_file.parts or "artifacts" in python_file.parts:
            continue
        try:
            py_compile.compile(str(python_file), doraise=True)
        except py_compile.PyCompileError as error:
            errors.append(f"Python syntax error: {python_file.relative_to(ROOT)}: {error}")

    if errors:
        print("Repository verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository verification: PASS")
    print(f"- stages: {len(STAGES)}")
    print(f"- required files per stage: {len(REQUIRED_STAGE_FILES)}")
    print("- local Markdown links: valid")
    print("- check/exercise API: consistent")
    print("- Python syntax: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
