"""
super_function.py
4 примера: super() для вызова родительского __init__ и методов.
"""

# 1) super() в __init__
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, interest_percent: float = 5.0):
        super().__init__(owner, balance)
        self.interest_percent = interest_percent


# 2) super() для расширения метода
class Logger:
    def log(self, message: str) -> str:
        return f"[LOG] {message}"


class FileLogger(Logger):
    def log(self, message: str) -> str:
        base = super().log(message)
        return base + " (saved to file)"


# 3) super() + цепочка наследования
class Device:
    def __init__(self, name: str):
        self.name = name


class Phone(Device):
    def __init__(self, name: str, os_name: str):
        super().__init__(name)
        self.os_name = os_name


class SmartPhone(Phone):
    def __init__(self, name: str, os_name: str, has_nfc: bool):
        super().__init__(name, os_name)
        self.has_nfc = has_nfc


# 4) super() в методе “описания”
class Employee:
    def describe(self) -> str:
        return "Employee"


class Manager(Employee):
    def describe(self) -> str:
        return super().describe() + " -> Manager"


if __name__ == "__main__":
    savings = SavingsAccount("Ali", 100, interest_percent=7.5)
    print("Example 1:", savings.owner, savings.balance, savings.interest_percent)

    logger = FileLogger()
    print("Example 2:", logger.log("Hello"))

    phone = SmartPhone("Pixel", "Android", has_nfc=True)
    print("Example 3:", phone.name, phone.os_name, phone.has_nfc)

    manager = Manager()
    print("Example 4:", manager.describe())
