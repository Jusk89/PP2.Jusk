"""
method_overriding.py
4 примера: переопределение методов (override), иногда с super(), иногда полностью.
"""

# 1) Полное переопределение
class Bird:
    def move(self) -> str:
        return "Bird moves"


class Penguin(Bird):
    def move(self) -> str:
        return "Penguin swims"


# 2) Переопределение + super() (расширяем текст)
class Notification:
    def send(self, text: str) -> str:
        return f"Sending: {text}"


class EmailNotification(Notification):
    def send(self, text: str) -> str:
        return super().send(text) + " via Email"


# 3) Переопределение для изменения логики (скидки)
class PriceCalculator:
    def final_price(self, base_price: float) -> float:
        return base_price


class VipPriceCalculator(PriceCalculator):
    def final_price(self, base_price: float) -> float:
        return base_price * 0.8  # VIP -20%


# 4) Одинаковый метод у разных наследников (полиморфизм)
class PaymentMethod:
    def pay(self, amount: float) -> str:
        return f"Pay {amount}"


class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} by card"


class CashPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} in cash"


if __name__ == "__main__":
    penguin = Penguin()
    print("Example 1:", penguin.move())

    email = EmailNotification()
    print("Example 2:", email.send("Your code is ready"))

    vip = VipPriceCalculator()
    print("Example 3:", vip.final_price(1000))

    payments: list[PaymentMethod] = [CardPayment(), CashPayment()]
    print("Example 4:", [p.pay(99.9) for p in payments])
