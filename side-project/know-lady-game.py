# Know lady characters ["Avril", "Serena", "Nico", "Leah", "Nikita", "Ada"]

import random

crush_list = []

print("*** Choosing your crush in the Knowledge or know lady game. ***")
print("Enter your crush name, type 'q' to quit.") 

# Chat GPT SOLUTION
'''Trong Python:
Danh sách trống sẽ được coi là False.
Danh sách có phần tử sẽ được coi là True.'''

while True: # while `True` giúp lặp vô hạn cho đến khi bạn muốn thoát.
    input_name = input("Who is your crush: ").title()
    if input_name.lower() == 'q': # Nếu người dùng nhập "q", thoát khỏi vòng lặp bằng lệnh `break``.
        break
    crush_list.append(input_name)

# Kiểm tra nếu danh sách crush_list không rỗng trước khi chọn ngẫu nhiên
if crush_list:
    print(f"Here are your crushes: {', '.join(crush_list)}")
    your_crush = random.choice(crush_list)
    print(f"Your love is: {your_crush}")
else:
    print("You didn't add any crush.")


# MY CODE

'''input_name = str(input("Who are your crush: "))
crush_list.append(input_name)

while input_name != "q":
  input_name = str(input("Anyone else: "))
  crush_list.append(input_name)

print(crush_list)

random_crush = random.randint(0, len(crush_list) -2)
your_crush = crush_list[random_crush]
print(your_crush)
'''
