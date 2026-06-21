def summarize_products(
    products: list[dict[str, object]], low_stock_threshold: int
) -> dict[str, object]:
    """상품의 전체 재고, 최고가 상품, 재고 부족 상품을 반환합니다."""
    if not products:
        raise ValueError("products는 비어 있을 수 없습니다.")

    total_stock = 0
    most_expensive_name = ""
    highest_price = float("-inf")
    low_stock_names: list[str] = []

    for product in products:
        name = str(product["name"])
        price = float(product["price"])
        stock = int(product["stock"])

        total_stock += stock
        if price > highest_price:
            highest_price = price
            most_expensive_name = name
        if stock <= low_stock_threshold:
            low_stock_names.append(name)

    return {
        "total_stock": total_stock,
        "most_expensive": most_expensive_name,
        "low_stock": low_stock_names,
    }


def main() -> None:
    products = [
        {"name": "notebook", "price": 3500, "stock": 4},
        {"name": "pen", "price": 1200, "stock": 12},
        {"name": "mug", "price": 9000, "stock": 2},
    ]
    print(summarize_products(products, low_stock_threshold=3))


if __name__ == "__main__":
    main()
