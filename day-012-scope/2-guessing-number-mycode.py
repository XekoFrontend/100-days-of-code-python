import random, art, os

def clear():
  # for window
  if os.name == "nt":
    _ = os.system('cls')
  # Mac or Linus ...
  else:
    _os.system('clear')

def play_game():
  HIDING_NUMBER = random.choice(range(1, 101))
  # easy_level = 10
  # hard_level = 5
  print(f"number for testing {HIDING_NUMBER}")

  def is_number(guess, HIDING_NUMBER):
    if guess > HIDING_NUMBER:
      return "Too high!"
    elif guess < HIDING_NUMBER:
      return "Too low!"
    else:
      return True

  play_game = True
  while play_game:
    # chose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guess = int(input("Guess a number: "))
    checking = is_number(guess, HIDING_NUMBER)
    print(checking)
    if checking == True:
      play_game = False
      print(f"Correct! the hiding number is {HIDING_NUMBER}")

# Chơi ván khác hoặc thoát game
while input("Do you want to play Guessing number game? (y/n):").lower() == "y":
  clear()
  print(art.logo)
  play_game()