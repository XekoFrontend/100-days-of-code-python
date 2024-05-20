print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2
  if extra_cheese == 'Y':
    bill += 1
  print(f"Your final bill is: ${bill}.")

elif size == 'M':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
  print(f"Your final bill is: ${bill}.")

elif size == 'L':
  bill = 25
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
  print(f"Your final bill is: ${bill}.")


# Angela's solution
"""
# Variable keeps track of the ongoing price.
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
"""

