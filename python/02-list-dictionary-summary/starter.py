def summarize_products(
    products: list[dict[str, object]], low_stock_threshold: int
) -> dict[str, object]:
    """상품 목록의 재고와 가격 정보를 요약합니다."""
    raise NotImplementedError("상품 요약 함수를 구현하세요.")


if __name__ == "__main__":
    sample_products = [
        {"name": "notebook", "price": 3500, "stock": 4},
        {"name": "pen", "price": 1200, "stock": 12},
        {"name": "mug", "price": 9000, "stock": 2},
    ]
    print(summarize_products(sample_products, low_stock_threshold=3))
