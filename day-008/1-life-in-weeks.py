# for an approximate result, multiply the time value by 52.1428571 weeks in one year.
# Example: input 56 output 1768 weeks
age = int(input("Enter your age: "))

def life_in_weeks(age):
    one_year = 52
    in_90_years = one_year * 90
    your_weeks = one_year * age
    your_weeks_left = in_90_years - your_weeks
    print(f"You have {your_weeks_left} weeks left.")
    
life_in_weeks(age)