users_list = []
pass_list = []

# TODO: export to .txt files

user_name = str(input("User name: "))
pass_word = str(input("Pass word: "))

def sign_up(user_name, pass_word):
  users_list.append(user_name)
  pass_list.append(pass_word)
  print("You have signed user name:", users_list[-1])
  print("You have signed password:", pass_list[-1])
  
sign_up(user_name, pass_word)


# TODO: login, for loop to find the correct pass in the list
input_pass= input("Enter your password: ")

while pass_list[-1] != input_pass:
  print("You password is incorrectly, please try again!")
  input_pass= input("Enter your password: ")

print("You password is correctly. Welcome! 😊")





# users_list.append("nam")
# users_list.extend(["thu", "tung", "tu"])
# users_list.insert(3, "hoa")




