#  This exercise applies the concepts of importing modules, using the random library, and conditional statements using if-else blocks.

import random
import my_ascii_art

game_images = [my_ascii_art.rock, my_ascii_art.paper, my_ascii_art.scissors]

user_input = input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
user_chose = int(user_input)
computer_chose = random.randint(0,2)

if 0 <= user_chose <= 2: 
  print(f"Your chose\n{game_images[user_chose]}")
  print(f"Computer chose\n{game_images[computer_chose]}")

if user_chose == 0 and computer_chose == 2:  
  print("You win!")
elif user_chose == 0 and computer_chose == 1:
  print("You lose!")
elif user_chose == 1 and computer_chose == 0:
  print("You win!")
elif user_chose == 1 and computer_chose == 2:
  print("You lose!")
elif user_chose == 2 and computer_chose == 1:
  print("You win!")
elif user_chose == 2 and computer_chose == 0:
  print("You lose!")
elif user_chose == computer_chose:
  print("Draw")
else:
  print("Type 0 for Rock, 1 for Paper or 2 for Scissors")


# Angela's code solution