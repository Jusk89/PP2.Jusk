x = lambda a : a + 10
print(x(5))  #Lambda Functions

"""
lambda_basics.py
4 примера: базовый синтаксис lambda, сравнение с обычной функцией, небольшие кейсы.
"""

# 1) lambda: квадрат числа
square = lambda number: number * number

# 2) lambda: проверка чётности
is_even = lambda number: number % 2 == 0

# 3) lambda: “мини-калькулятор” через словарь операций
operations = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}

# 4) lambda: ключ сортировки по длине строки (используем отдельно позже)
length_key = lambda text: len(text)


if __name__ == "__main__":
    print("Example 1:", square(7))

    print("Example 2:", is_even(10), is_even(9))

    print("Example 3:", operations["add"](2, 3), operations["mul"](4, 5))

    words = ["hi", "Python", "ok", "developer"]
    print("Example 4:", sorted(words, key=length_key))
