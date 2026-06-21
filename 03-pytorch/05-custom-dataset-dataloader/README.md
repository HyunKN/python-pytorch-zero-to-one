# 05 — Custom Dataset과 DataLoader

## 무엇을 배우나

image path와 label 목록을 PyTorch `Dataset`으로 만들고 DataLoader batch로 변환합니다.

## 1. 완성 예제 실행

```powershell
python 03-pytorch/05-custom-dataset-dataloader/demo.py
```

demo는 임시 RGB image 두 장을 만들어 `(2, 3, 16, 16)` batch를 출력합니다.

## 2. 코드 흐름

1. `__len__()`은 sample 개수를 반환합니다.
2. `__getitem__()`은 index에 해당하는 path와 label을 찾습니다.
3. Pillow로 image를 열고 RGB로 변환합니다.
4. transform을 적용해 Tensor로 바꿉니다.
5. DataLoader가 여러 sample을 batch로 묶습니다.

transform을 필수 parameter로 두어 `__getitem__()`이 항상 Tensor를 반환하도록 type contract를 명확히 했습니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `ImageClassificationDataset`을 구현합니다.

```powershell
python 03-pytorch/05-custom-dataset-dataloader/check.py
```

## 완료 기준

- image와 label 연결이 정확함
- RGB Tensor shape 설명
- lazy loading의 의미 설명
- [notes.md](notes.md) 작성
