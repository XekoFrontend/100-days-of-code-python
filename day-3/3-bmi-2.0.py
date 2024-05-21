print("*** BMI 2.0 ***")
# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight."
)
elif 25 > bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 30 > bmi >= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 35 > bmi >= 30:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")



"""
Angela's solution:

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight."
)
elif bmi < 25:
print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
  ...
"""
