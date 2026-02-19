def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")     #Arguments


def y_function(name): # name is a parameter
  print("Hello", name)

y_function("Emil") # "Emil" is an argument


def function(fname, lname):
  print(fname + " " + lname)

function("Emil", "Refsnes")  #Number of Arguments   
'''
By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.
'''

def Vy_function(name = "friend"):
  print("Hello", name)

Vy_function("Emil")
Vy_function("Tobias")
Vy_function()
Vy_function("Linus")   #Default Parameter Values

def Ey_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

Ey_function(animal = "dog", name = "Buddy")

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)                     #Passing Different Data Types
