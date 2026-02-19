"""
lambda_with_filter.py
4 примера: filter + lambda для отбора элементов.
"""

# 1) Оставить только чётные числа
def only_even(numbers: list[int]) -> list[int]:
    return list(filter(lambda n: n % 2 == 0, numbers))


# 2) Оставить только “длинные” слова
def only_long_words(words: list[str], min_length: int = 5) -> list[str]:
    return list(filter(lambda w: len(w) >= min_length, words))


# 3) Оставить только положительные значения
def only_positive(values: list[int]) -> list[int]:
    return list(filter(lambda v: v > 0, values))


# 4) Оставить только товары “в наличии”
def in_stock(products: list[dict]) -> list[dict]:
    return list(filter(lambda p: p.get("stock", 0) > 0, products))


if __name__ == "__main__":
    print("Example 1:", only_even([1, 2, 3, 4, 5, 6]))

    print("Example 2:", only_long_words(["hi", "python", "code", "developer"], min_length=4))

    print("Example 3:", only_positive([-2, 0, 7, -1, 3]))

    items = [
        {"name": "Keyboard", "stock": 3},
        {"name": "Mouse", "stock": 0},
        {"name": "Monitor", "stock": 2},
    ]
    print("Example 4:", in_stock(items))
