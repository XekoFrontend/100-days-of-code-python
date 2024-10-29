user_data = {} # Empty dictionary
print("Who is the tallest person?")
  
continue_program = True
while continue_program:
  name = input("Type your name:\n")
  height = int(input("Type your height (cm):\n"))
  exit_program = input("Type 'yes' to continues, Otherwise, type 'no' to exit.\n")

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
    list_keys.append(key)
    list_values.append(user_data[key])
    for value in list_values:
      if value > highest:
        highest = value
  
  highest_location = list_values.index(highest)
  print(f"{list_keys[highest_location]} is tall {highest} cm who is the tallest person.")

tallest_person(name, height)

######################
# Get the highest value
# highest = max(user_data.values())