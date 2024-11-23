from random import randint
import art, os

def clear():
  # for window
  if os.name == "nt":
    _ = os.system('cls')
  # Mac or Linus ...
  else:
    _os.system('clear')

# 4.1 Create Lever turns Global scope
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# 3. Function to check user's guess against  actual answer.
def check_answer(user_guess, actual_answer, turns):
  """Check answer against guess, return the number of turns remaining."""
  if user_guess > actual_answer:
    print("Too high!")
    return turns - 1
  elif user_guess < actual_answer:
    print("Too low!")
    return turns - 1
  else:
    print(f"You got it! The answer was {actual_answer}.")

# 4. Function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "hard":
    return HARD_LEVEL_TURNS
  else:
    return EASY_LEVEL_TURNS

# 5.1 Create a game function
def game():
  print(art.logo)
  # 1. Generate a random number between 1 and 100.
  answer = randint(1, 100)
  #4.2 Call the difficulty function and notify the remaining turns.
  turns = set_difficulty() # Global variable
  # 5. Repeat the guessing function if they get wrong
  guess = 0 # Temp variable define
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number. ")
    # 2. Let the user guess a number.
    guess = int(input("Guess a number: "))
    turns = check_answer(user_guess=guess, actual_answer=answer, turns=turns)
    # 6 Track the number of turns and reduce by 1 if they get it wrong
    if turns == 0:
      print("You've run out of guess. You lose!")
      return # Thoát khỏi function
    # elif guess != answer:
    #   print("Guess again!")

# Chơi ván khác hoặc thoát game
while input("Do you want to play Guessing number game? (y/n):").lower() == "y":
  clear()
  game()