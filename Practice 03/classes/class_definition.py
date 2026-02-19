

#  Класс "Dog"
class Dog:
    def __init__(self, name: str):
        self.name = name

    def bark(self) -> str:
        return f"{self.name}: Woof!"


# 2) Класс "BankAccount"
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def info(self) -> str:
        return f"{self.owner} balance: {self.balance:.2f}"


# 3) Класс "Book"
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self) -> str:
        return f"'{self.title}' by {self.author}"


# 4) Класс "Timer" (простая логика “тикать”)
class Timer:
    def __init__(self):
        self.seconds = 0

    def tick(self, step: int = 1) -> int:
        self.seconds += step
        return self.seconds


if __name__ == "__main__":
    dog = Dog("Rex")
    print("Example 1:", dog.bark())

    account = BankAccount("Aigerim", 100)
    account.deposit(50)
    print("Example 2:", account.info())

    book = Book("Clean Code", "Robert C. Martin")
    print("Example 3:", book.describe())

    timer = Timer()
    print("Example 4:", timer.tick(), timer.tick(5))
