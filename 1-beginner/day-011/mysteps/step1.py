import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# for card in cards:
#   player.append

# random_index = random.randint(0, len(cards) - 1)
# player_card = cards[random_index]
# print(player_card)


# 1. Chia bài cho player
player_cards = []
while len(player_cards) < 2:
  random_card = player_cards.append(random.choice(cards))
 # Tính điểm 
player_current_score = 0
for score in player_cards:
  player_current_score += score
print(f"Your card {player_cards}, current score: {player_current_score}")


# 2. Computer
computer_cards = []
while len(computer_cards) < 2:
  random_card = computer_cards.append(random.choice(cards))
 # Tính điểm 
computer_current_score = 0
for score in computer_cards:
  computer_current_score += score
print(f"Computer card {computer_cards[0]}")
print(computer_cards, computer_current_score)

#TODO: Chuyển phần chia bài thành function, do bị lặp lại code