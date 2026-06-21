from collections.abc import Callable
from pathlib import Path

import torch
from PIL import Image
from torch.utils.data import Dataset


class ImageClassificationDataset(Dataset):
    def __init__(
        self,
        samples: list[tuple[Path, int]],
        transform: Callable[[Image.Image], torch.Tensor],
    ) -> None:
        raise NotImplementedError("Dataset 초기화를 구현하세요.")

    def __len__(self) -> int:
        raise NotImplementedError("Dataset 길이를 반환하세요.")

    def __getitem__(self, index: int) -> tuple[torch.Tensor, int]:
        raise NotImplementedError("이미지와 label 읽기를 구현하세요.")
