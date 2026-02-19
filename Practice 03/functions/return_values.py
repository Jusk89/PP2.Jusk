"""
return_values.py
4 примера: возврат одного значения, нескольких значений, ранний return, возврат коллекций.
"""

from typing import Tuple


# 1) Возврат одного значения
def average_score(scores: list[int]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# 2) Возврат нескольких значений (tuple)
def min_max(numbers: list[int]) -> Tuple[int, int]:
    return min(numbers), max(numbers)


# 3) Ранний return (валидация)
def divide_numbers(dividend: float, divisor: float) -> float | None:
    if divisor == 0:
        return None
    return dividend / divisor


# 4) Возврат словаря (результат “под отчёт”)
def build_grade_report(student_name: str, scores: list[int]) -> dict:
    avg = average_score(scores)
    return {
        "student": student_name,
        "scores": scores,
        "average": round(avg, 2),
        "passed": avg >= 60,
    }


if __name__ == "__main__":
    print("Example 1:", average_score([80, 90, 70]))

    print("Example 2:", min_max([5, 1, 9, 3]))

    print("Example 3:", divide_numbers(10, 2), divide_numbers(10, 0))

    print("Example 4:", build_grade_report("Dana", [100, 55, 70]))
