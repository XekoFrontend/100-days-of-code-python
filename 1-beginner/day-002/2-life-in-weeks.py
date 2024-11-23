# How many weeks we have left, if we live until 90 years old.

age = input("How old are you?\n")
current_age = int(age)
remaining_age = 90 - current_age
# A year has 52 weeks (leap year is 53 weeks)
remaining_week = remaining_age * 52

print(f"You have {remaining_age} year left.")
print(f"You have {remaining_week} weeks left.")