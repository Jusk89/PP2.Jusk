class Animal:
    def __init__(self,name):
        self.name = name
    
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print (f"{self.name}: Wow ")



class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f"{self.name}: Meow ") 
    
Murka = Cat("murka")
Murka.sound()
