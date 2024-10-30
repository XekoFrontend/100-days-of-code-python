# "This program applies knowledge lists and nested list."
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?\n")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower() # Lấy ký tự đầu là chữ cái của input.
abc = ["a", "b", "c"] # list tạm dùng để so vị trí của chữ cái khi input. Đại diện cho các cột A B C.

letter_index = abc.index(letter) # Xác định vị trí của chữ cái được input sau khi so với list tạm abc. A = 0, B =1, C =2
number_index = int(position[1]) - 1 # Vì vị trí trong list bắt đầu bằng 0 nên, các số sau input phải - 1. Ex: 1-1=0, 2-1=1, 3-1=2b2

map[number_index][letter_index] = "X" # Vì nested list đi từ ngoài vào trong, mà phần print xuất ra thành hàng và cột.
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
