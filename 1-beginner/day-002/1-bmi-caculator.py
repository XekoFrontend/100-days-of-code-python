# 1st input: enter height in meters e.g: 1.65
height = input("Enter height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter weight in kilograms: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)

print("Your BMI is:")
print(bmi_as_int)