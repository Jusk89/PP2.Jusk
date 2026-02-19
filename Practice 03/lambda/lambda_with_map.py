"""
lambda_with_map.py
4 примера: map + lambda для преобразований.
"""

# 1) Увеличить все цены на 10%
def increase_prices(prices: list[float]) -> list[float]:
    return list(map(lambda price: round(price * 1.10, 2), prices))


# 2) Превратить список строк в список их длин
def get_lengths(words: list[str]) -> list[int]:
    return list(map(lambda word: len(word), words))


# 3) Из градусов C сделать F
def convert_temps(celsius_values: list[float]) -> list[float]:
    return list(map(lambda c: (c * 9 / 5) + 32, celsius_values))


# 4) Объединить имена и фамилии в "Имя Фамилия"
def combine_names(first_names: list[str], last_names: list[str]) -> list[str]:
    return list(map(lambda pair: f"{pair[0]} {pair[1]}", zip(first_names, last_names)))


if __name__ == "__main__":
    print("Example 1:", increase_prices([100, 250.5, 80]))

    print("Example 2:", get_lengths(["cat", "elephant", "python"]))

    print("Example 3:", convert_temps([0, 25, 100]))

    print("Example 4:", combine_names(["Ali", "Dana"], ["Khan", "Nur"]))
