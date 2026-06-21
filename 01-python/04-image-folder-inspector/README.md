# 04 — 이미지 폴더 검사

## 무엇을 배우나

폴더를 재귀적으로 탐색하고 이미지 확장자만 선택해 개수를 집계합니다. 실제 ML dataset을 확인하기 전에 사용하는 기본 검사입니다.

## 1. 완성 예제 실행

```powershell
python 01-python/04-image-folder-inspector/demo.py
```

demo가 임시 폴더와 파일을 만들고 자동으로 정리합니다. 이미지가 아닌 `notes.txt`는 결과에서 제외되어야 합니다.

예상 결과:

```python
{"total": 3, "by_extension": {".jpeg": 1, ".jpg": 1, ".png": 1}}
```

## 2. 코드 흐름

1. `Path.rglob("*")`로 모든 하위 파일을 확인합니다.
2. suffix를 소문자로 바꿉니다.
3. 허용한 이미지 확장자인 경우에만 개수를 더합니다.
4. 확장자별 개수와 전체 합을 반환합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `inspect_image_folder()`를 구현합니다.

```powershell
python 01-python/04-image-folder-inspector/check.py
```

## 완료 기준

- 대문자 확장자도 올바르게 처리
- 하위 폴더 포함
- 이미지가 아닌 파일 제외
- [notes.md](notes.md) 작성
