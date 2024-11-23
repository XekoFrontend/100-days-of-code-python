import art

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

print(art.logo)
def calculator():  
  n1 = float(input("Enter the first number: "))
  should_accumulate = True
  while should_accumulate:
    # Show operation symbols
    for key in operation: 
      print(key)
    operation_symbol = input("Pick an operation: ")
    n2 = float(input("Enter the next number: "))
    # Assign operation to math functions
    answer = operation[operation_symbol](n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}") # Show the math

    choice = input(f"Type 'y' continue calculating with {answer} or type 'n' to new calculating. Type 'q' to quit app.\n")
    if choice == "y":
      n1 = answer
    elif choice == 'n':
      should_accumulate = False
      print("\n" * 20) # Gỉa lập clear màn hình terminal.
      calculator()
    else:
      # Quit app completely.
      return False

calculator()