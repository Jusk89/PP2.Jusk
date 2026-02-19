"""
multiple_inheritance.py
4 примера: множественное наследование, порядок MRO, mixin-подход.
"""

# 1) Два “умения” через mixin
class FlyMixin:
    def fly(self) -> str:
        return "I can fly"


class SwimMixin:
    def swim(self) -> str:
        return "I can swim"


class Duck(FlyMixin, SwimMixin):
    pass


# 2) MRO (Method Resolution Order): кто победит, если методы одинаковые
class A:
    def hello(self) -> str:
        return "Hello from A"


class B:
    def hello(self) -> str:
        return "Hello from B"


class C(A, B):
    pass


# 3) mixin для логирования + основной класс
class LogMixin:
    def log(self, message: str) -> str:
        return f"[LOG] {message}"


class Service(LogMixin):
    def run(self) -> str:
        return self.log("Service started")


# 4) super() в множественном наследовании (кооперативное наследование)
class Base:
    def __init__(self):
        self.steps: list[str] = ["Base"]


class StepOne(Base):
    def __init__(self):
        super().__init__()
        self.steps.append("StepOne")


class StepTwo(Base):
    def __init__(self):
        super().__init__()
        self.steps.append("StepTwo")


class Pipeline(StepOne, StepTwo):
    # Важно: MRO будет вызывать StepOne -> StepTwo -> Base
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    duck = Duck()
    print("Example 1:", duck.fly(), duck.swim())

    c = C()
    print("Example 2:", c.hello())
    print("Example 2 MRO:", [cls.__name__ for cls in C.mro()])

    service = Service()
    print("Example 3:", service.run())

    pipeline = Pipeline()
    print("Example 4:", pipeline.steps)
    print("Example 4 MRO:", [cls.__name__ for cls in Pipeline.mro()])
