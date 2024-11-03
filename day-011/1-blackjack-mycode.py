import random, art, os

def clear():
  '''clear VS code terminal'''
  # for Windows
  if os.name == 'nt':
      _ = os.system('cls')
  # Mac or Linux (aka posix)
  else:
      _ = os.system('clear')

def deal_card():
  """Random a card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards."""
  # Tạo dấu diệu để nhận diện Black jack.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # Chuyển đổi Ace card điểm 11 sang 1, nếu tổng điểm lớn hơn 21.
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11) # cards mean 'user_cards' or 'computer_cards'.
    cards.append(1)
  # Trả về tổng điểm của 1 list (cards) sau khi đã xét qua 2 điều kiện phía trên.
  return sum(cards)

def compare(user_score, computer_score, user_cards, computer_cards):
  if user_score ==  computer_score:
    return "Draw. 🤗"
  elif user_score == 0:
    return "You have BlackJack 💪.\nYou win. 🎉"
  elif computer_score == 0:
    return "Computer has BlackJack.\nou lose. 💀"
  elif user_score > 21:
    return "You lose. 💀"
  elif user_score < 22 and len(user_cards) == 5:
    return "You have Five Spirits 👼.\nYou win. 🎉"
  elif computer_score < 22 and len(computer_cards) == 5:
    return "Computer has Five Spirits.\nYou lose. 💀"
  elif user_score > computer_score or computer_score > 21:
    return "You win. 🎉"
  else:
    return "You lose. 💀"

def play_game():
  print(art.logo)
  user_cards = []
  computer_cards = []  
    # Chia bài
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_game_over = False
  while not is_game_over:
  # Gọi hàm tính điểm calculate_score
    user_score = calculate_score(cards=user_cards)
    computer_score = calculate_score(cards=computer_cards)
    print(f"User cards: {user_cards} and score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card. Type 'n' to pass.\n ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
    

  while computer_score != 0 and computer_score < 16:
    computer_cards.append(deal_card())
    computer_score = calculate_score(cards=computer_cards)

  game_result = compare(user_score, computer_score, user_cards, computer_cards)
  print(f"{" "*20}🏆\nYour final cards: {user_cards} and score: {user_score}")
  print(f"Computer's final card: {computer_cards} and score: {computer_score}")
  print(game_result)

while input("Do you want to play a BlackJack game (y/n):") == 'y':
  clear()
  play_game()
  
  

    
      
    