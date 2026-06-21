from exercise import summarize_products


def main() -> int:
    products = [
        {"name": "notebook", "price": 3500, "stock": 4},
        {"name": "pen", "price": 1200, "stock": 12},
        {"name": "mug", "price": 9000, "stock": 2},
    ]
    try:
        result = summarize_products(products, low_stock_threshold=3)
        assert result == {
            "total_stock": 18,
            "most_expensive": "mug",
            "low_stock": ["mug"],
        }
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: List와 Dictionary 요약")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
