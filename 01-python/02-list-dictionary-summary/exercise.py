import collections
def summarize_products(
    products: list[dict[str, object]], low_stock_threshold: int
) -> dict[str, object]:
    """상품 목록의 재고와 가격 정보를 요약합니다."""
    # raise NotImplementedError("상품 요약 함수를 구현하세요.")
    if not products:
        raise ValueError("projucts가 비어있습니다.")

    # 필요한 것: 1. total_stock 2. most_expensive 3. low_stock 리스트(이름=문자열)
    total_stock = 0
    most_expensive = ""
    low_stocks: list[str] = []
    highest_price = float("-inf")

    for product in products:
        # 필요한것 한 루프당 각각 product로 1개씩 가져와서
        # stock을 더해줌, 가장 비싼것을 갱신, low_stock list추가(append)
        name = str(product["name"])
        stock = int(product["stock"])
        price = float(product["price"])

        total_stock += stock
        
        if highest_price < price:
            most_expensive = name
            highest_price = price
        
        if stock <= low_stock_threshold:
            low_stocks.append(name)

    return {
        "total_stock": total_stock,
        "most_expensive": most_expensive,
        "low_stock": low_stocks,
    }

if __name__ == "__main__":
    sample_products = [
        {"name": "notebook", "price": 3500, "stock": 4},
        {"name": "pen", "price": 1200, "stock": 12},
        {"name": "mug", "price": 9000, "stock": 2},
    ]
    print(summarize_products(sample_products, low_stock_threshold=3))
