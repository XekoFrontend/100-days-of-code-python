#Step 1 
import random
print('*** Manga characters guessing game ***'.upper())
word_list = ["doraemon", "songoku", "kirimaru"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"The word has {len(chosen_word)} letters.")
if word_list.index(chosen_word) == 0:
  print("This is a manga fat robot cat.")
elif word_list.index(chosen_word) == 1:
  print("Earth’s mightiest warrior with a heart as big as his appetite.")
elif word_list.index(chosen_word) == 2:
  print("This is a stingy, money-grubbing manga boy at the ninja training school.")
# Print placeholder ____ and hide chosen word
placeholder = "🕵️‍♀️  "
for i in range(0, len(chosen_word)):
  placeholder += "_"
print(placeholder)

correct_letters = [] # Save correct letters, avoid reset after each loop
lives = 5
game_over = False
while not game_over:
  #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input(str("Guess a letter: ")).lower()
  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  display = "🕵️‍♀️ " # Display placeholder and correct letter
  for letter in chosen_word:
    if letter == guess: 
      display += guess
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"
  print(display)
  # Check if guess letter is wrong will reduce one life and remaining life.
  if guess not in chosen_word:
    lives -= 1
    print(f"You have {lives} lives left.")
  # Check win or lose
  checking = display.count("_")
  if checking == 0:
    game_over = True
    print("🎉  Your answer is correctly.")
  elif lives == 0:
    game_over = True
    print("💀  Your lose.")





# COMMENT:
#         1. Mình bị mắc kẹt ở đoạn in "_" do hướng đến việc dùng list để ẩn từ khóa. Trong khi giải pháp đơn giản hơn là dùng dấu cộng (+) để nối các ký tự.
#         2. Sử dụng  - in - trong (if "_" not in display:) để kiểm tra ký tự trong display thay cho (checking = display.count("_")), sau đó tạo 1 - elif - để xem ký tự đã có trong danh sách correct_letters và cộng tiếp vô display luôn.

