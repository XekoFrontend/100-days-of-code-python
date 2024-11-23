# Example input: Angela, Ben, Jenny, Michael, Chloe
import random

names_string = input("Enter names followed by comma then space: ")
names = names_string.split(", ")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
names_length = len(names) - 1
random_number = random.randint(0, names_length)
name_selected = names[random_number]
print(f"{name_selected} is going to buy the meal today!")