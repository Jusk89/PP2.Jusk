"""
lambda_with_sorted.py
4 примера: sorted + lambda (сортировка по ключу).
"""

# 1) Сортировка чисел по модулю
def sort_by_absolute(numbers: list[int]) -> list[int]:
    return sorted(numbers, key=lambda n: abs(n))


# 2) Сортировка слов по длине
def sort_words_by_length(words: list[str]) -> list[str]:
    return sorted(words, key=lambda w: len(w))


# 3) Сортировка списка словарей по цене
def sort_products_by_price(products: list[dict]) -> list[dict]:
    return sorted(products, key=lambda p: p["price"])


# 4) Сортировка студентов по среднему баллу (по убыванию)
def sort_students_by_grade(students: list[dict]) -> list[dict]:
    return sorted(students, key=lambda s: s["avg_grade"], reverse=True)


if __name__ == "__main__":
    print("Example 1:", sort_by_absolute([3, -10, 2, -1, 0]))

    print("Example 2:", sort_words_by_length(["a", "python", "to", "code"]))

    products = [
        {"name": "Phone", "price": 1200},
        {"name": "Case", "price": 20},
        {"name": "Laptop", "price": 2000},
    ]
    print("Example 3:", sort_products_by_price(products))

    students = [
        {"name": "Dana", "avg_grade": 88},
        {"name": "Ali", "avg_grade": 92},
        {"name": "Tim", "avg_grade": 75},
    ]
    print("Example 4:", sort_students_by_grade(students))
