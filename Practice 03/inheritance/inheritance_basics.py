#Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
 # 2) Vehicle -> Bike (наследуем поля и методы)
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def info(self) -> str:
        return f"Brand: {self.brand}"


class Bike(Vehicle):
    def ring_bell(self) -> str:
        return "Ring-ring!"


# 3) Person -> Student (добавляем новое поле)
class Person:
    def __init__(self, full_name: str):
        self.full_name = full_name


class SchoolStudent(Person):
    def __init__(self, full_name: str, grade: int):
        super().__init__(full_name)
        self.grade = grade


# 4) Shape -> Circle (полиморфизм через один метод area)
class Shape:
    def area(self) -> float:
        return 0.0


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius * self.radius


if __name__ == "__main__":
    cat = Cat("Murka")
    print("Example 1:", cat.speak())

    bike = Bike("Giant")
    print("Example 2:", bike.info(), bike.ring_bell())

    student = SchoolStudent("Dana Nur", grade=10)
    print("Example 3:", student.full_name, student.grade)

    shapes: list[Shape] = [Shape(), Circle(2)]
    print("Example 4:", [s.area() for s in shapes])