"""테스트용 샘플 이미지(sample.png)를 생성합니다."""

import numpy as np
from PIL import Image

# 4x4 크기의 RGB 이미지를 NumPy 배열로 직접 생성
pixels = np.array(
    [
        [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]],  # 빨강 초록 파랑 노랑
        [[255, 165, 0], [128, 0, 128], [0, 255, 255], [255, 192, 203]],  # 주황 보라 청록 분홍
        [[255, 255, 255], [128, 128, 128], [64, 64, 64], [0, 0, 0]],  # 흰색 회색 어두운회색 검정
        [[139, 69, 19], [34, 139, 34], [70, 130, 180], [255, 215, 0]],  # 갈색 숲녹색 강청색 금색
    ],
    dtype=np.uint8,
)  # shape: (4, 4, 3) — HWC 형태

image = Image.fromarray(pixels, mode="RGB")
image.save("02-numpy/02-image-normalization/sample.png")

print("sample.png 저장 완료!")
print(f"  - shape  : {pixels.shape}  (H=4, W=4, C=3)")
print(f"  - dtype  : {pixels.dtype}")
print(f"  - 픽셀 값 범위: {pixels.min()} ~ {pixels.max()}")
