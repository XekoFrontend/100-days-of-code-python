print("*** Welcome to the tip calculator! ***")

# Input and convert data type
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give?\n10, 12, or 15?\n%"))
people = int(input("How many people to split the bill?\n"))

# Calculate the tip amount
tip_amount =  tip / 100 * bill

# Calculate the total bill including the tip
bill_with_tip = bill + tip_amount

# Calculate the amount each person should pay, rounding to 2 decimal places
bill_per_person = bill_with_tip / people
final_bill = round(bill_per_person, 2)
# Another format: showing 2 decimal places
# final_bill = "{:.2f}".format(bill_per_person)

# Print the amount each person should pay
print(f"Each person should pay: ${final_bill}")





"""
Example Calculation:
If the tip percentage is 12% and the total bill is $150:
12/100 = 0.12
150 * 0.12 = 18 (tip amount)
150 + 18 = 168 (total with tip)
Alternatively, you can calculate the total with tip as:
150 * 1.12 = 168
Another way:
(150 / 5) * 1.12
"""
