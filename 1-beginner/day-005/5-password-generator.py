#Password Generator Project


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_choice = input("Do you want to choice an easy password or a hard password (e/h): ").lower()

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Example: input
# nr_letters = 4
# nr_symbols = 2
# nr_numbers = 2 

### --- 1. For loop ---
# set số lần loop, dựa vào input
loop_time_letters = range(0, nr_letters)
loop_time_symbols = range(0, nr_symbols)
loop_time_numbers = range(0, nr_numbers)

new_list = []

for letter in loop_time_letters:
  random_letters = random.randint(0, len(letters) -1)
  new_letter = letters[random_letters]
  add_to_list = new_list.append(new_letter)

for symbol in loop_time_symbols:
  random_letters = random.randint(0, len(symbols) -1)
  new_letter = symbols[random_letters]
  add_to_list = new_list.append(new_letter)

for letter in loop_time_numbers:
  random_letters = random.randint(0, len(numbers) -1)
  new_letter = numbers[random_letters]
  add_to_list = new_list.append(new_letter)

# ---------
# Another way is Use .join() to print the password from the list (⬇️ 2. While loop)
# password = ''.join(new_list)
# ---------

if nr_choice == "e":
  easy_password = ""
  for i in new_list:
    easy_password += i
  print(f"The easy password: {easy_password}")

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
elif nr_choice == 'h':
  random.shuffle(new_list)
  hard_password = ""
  for j in new_list:
    hard_password += j
  print(f"The hard password: {hard_password}")
else:
  print("Try again!")



### --- 2. While loop ---
'''
password = []
while nr_letters > 0:
    nr_letters -= 1
    letters_rand = random.choice(letters)
    password += letters_rand

while nr_numbers > 0:
    nr_numbers -= 1
    numbers_ran = random.choice(numbers)
    password += numbers_ran

while nr_symbols > 0:
    nr_symbols -= 1
    symbols_rand = random.choice(symbols)
    password.append(symbols_rand)


print(f"Eazy pass: {"".join(password)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
print(f"Hard pass: {"".join(password)}")
'''
