#  This exercise applies the concepts of importing modules, using the random library, list, and conditional statements using if-else blocks.

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
  print("You win!🎉")
elif user_chose == 0 and computer_chose == 1:
  print("You lose!😒")
elif user_chose == 1 and computer_chose == 0:
  print("You win!🎉")
elif user_chose == 1 and computer_chose == 2:
  print("You lose!😒")
elif user_chose == 2 and computer_chose == 1:
  print("You win!🎉")
elif user_chose == 2 and computer_chose == 0:
  print("You lose!😒")
elif user_chose == computer_chose:
  print("Draw. do you want a new turn.")
else:
  print("Your input is invalid. You must choose 0, 1 or 2.")


# Angela's code solution
# if user_choice >= 3 or user_chose < 0:
#   print("You typed an invalid number, you lose!")
# else:
#   print(game_images[user_choice])
#   computer_choice = random.randint(0, 2)
#   print(game_images[computer_choice])

#   if user_choice >= 3 or user_choice < 0: 
#     print("You typed an invalid number, you lose!") 
#   elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
#   elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
#   elif computer_choice > user_choice:
#     print("You lose")
#   elif user_choice > computer_choice:
#     print("You win!")
#   elif computer_choice == user_choice:
#     print("It's a draw")

'''
Step 1: Understand the rules: 2 > 1 > 0
Scissors (2) beats Paper (1).
Paper (1) beats Rock (0).
Rock (0) beats Scissors (2).
If both the user and the computer choose the same, it's a draw.

Step 2: Special Cases:
If the user chooses 0 (Rock) and the computer chooses 2 (Scissors), the user wins.
If both the user and the computer choose the same, it’s a draw.
If the computer chooses 0 (Rock) and the user chooses 2 (Scissors), the user loses.

Step 3: Determine the Winner
If the user’s choice is greater than the computer’s choice, the user wins.
If the user’s choice is less than the computer’s choice, the user loses.

Step 4: Handle Invalid Input
Print a message if the user enters a number outside of the range 0 - 2.
Place this validation in the first if statement.

Sumary:
1.Print a message if the user enters a number outside of 0 - 2. This should be the first check.
2. Compare the user’s choice with the computer’s choice.
3. Add the draw case if the user’s choice is the same as the computer’s choice.
4. Handle the case where the computer is 0 (Rock) and the user is 2 (Scissors) which means the user loses.
5. If the user’s choice is greater than the computer’s choice, the user wins.
'''