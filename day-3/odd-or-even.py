print("*** Welcom to Odd or Even Checker! ***")
number = int(input("Enter your number: "))
# IF the number can be divided by 2 with 0 remainder
if number % 2 == 0:
  print(f"{number} is an even number.")
else:
  print(f"{number} is an odd number.")