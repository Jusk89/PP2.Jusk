def my_function():#Creating a Function
  print("Hello from a function")   

  my_function() #Calling a Function

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))  #With functions, you write the code once and reuse it:


def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)   #Return Values


def my_function():
  pass      #The pass Statement