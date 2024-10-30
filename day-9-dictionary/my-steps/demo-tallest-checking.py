user_data = {} # Empty dictionary
print("Who is the tallest person?")
  
continue_program = True
while continue_program:
  name = input("Type your name:\n")
  height = int(input("Type your height (cm):\n"))
  exit_program = input("Do you want to continue. Type 'yes' or 'no'\n").lower()

  user_data[name] = height # Gắn giá trị values theo keys

  # Điều kiện để thoát chương trình
  if exit_program == "no":
    continue_program = False
  else:
    print("TO-DO: Clean screen")


def tallest_person(name, height):
  list_keys = []
  list_values = []
  highest = 0
  for key in user_data:
    # 1. Đưa từng giá trị key và value vô lần lượt các list_keys, list_values
    list_keys.append(key)
    list_values.append(user_data[key])
    # 2. Thuật toán tìm số lớn nhất. Thay thế bằng build in function: highest = max(user_data.values())
    for value in list_values:
      if value > highest:
        highest = value
  # 3. Lấy vị trí index của số lớn nhất trong list_values (height) làm tham chiếu cho list_keys (name)
  highest_location = list_values.index(highest)
  print(f"{list_keys[highest_location]} is tall {highest} cm who is the tallest person.")

tallest_person(name, height)
