# 1) Squares up to N
class Squares:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current ** 2
            self.current += 1
            return value
        else:
            raise StopIteration


# 2) Even numbers between 0 and n
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 2
            return value
        else:
            raise StopIteration


# 3) Numbers divisible by 3 and 4 (0..n)
class DivisibleBy3And4:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1
            if num % 3 == 0 and num % 4 == 0:
                return num
        raise StopIteration


# 4) Squares from a to b
class SquaresRange:
    def __init__(self, a, b):
        self.current = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.b:
            value = self.current ** 2
            self.current += 1
            return value
        else:
            raise StopIteration


# 5) Countdown from n to 0
class Countdown:
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration


# ----------------- TEST PART -----------------

# 1
n = int(input("Squares up to N: "))
print(",".join(str(i) for i in Squares(n)))

# 2
n = int(input("Even numbers up to N: "))
print(",".join(str(i) for i in EvenNumbers(n)))

# 3
n = int(input("Divisible by 3 and 4 up to N: "))
print(",".join(str(i) for i in DivisibleBy3And4(n)))

# 4
a = int(input("Squares from a: "))
b = int(input("to b: "))
print(",".join(str(i) for i in SquaresRange(a, b)))

# 5
n = int(input("Countdown from N: "))
print(",".join(str(i) for i in Countdown(n)))