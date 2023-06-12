from art10 import logo

print(logo)

a = float(input("Type the first num: "))

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

for key in operations.keys():
  print(key)

operation_symbol=input("Pick an operation from the line above: ")

b = float(input("Type the second num: "))

if operation_symbol not in operations.keys():
  print("Not a valid operator")
  quit()

function = operations[operation_symbol]
value = function(a,b)
print(f"{a} {operation_symbol} {b} = {value}")

to_cont=True
loop_value = value

while to_cont is True:

  y_or_n = input(f"Type 'y' to continue calculating with {loop_value}, or type 'n' to quit: ").lower()

  decision = ["y", "n"]

  if y_or_n not in decision:
    print("Not a valid input!")
    quit()

  if y_or_n=="n":
    to_cont = False
    quit()

  new_operation = input("Pick another operation: ")
  if new_operation not in operations.keys():
    print("Not a valid operator")
    quit()

  new_num = int(input("Type another number: "))
  new_function = operations[new_operation]
  new_value = new_function(loop_value, new_num)
  loop_value = new_value

  print(f"{loop_value} {new_operation} {new_num} = {new_value}")
