import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# 1. Chia bài
# TODO 1: Chuyển phần chia bài thành function, tránh bị lặp lại code
# 1.1 Player
player_cards = []
while len(player_cards) < 2:
  random_card = player_cards.append(random.choice(cards))
 # Tính điểm 
player_score = 0
for score in player_cards:
  player_score += score
print(f"Your card {player_cards}, current score: {player_score}")

# 1.2 Computer
computer_cards = []
while len(computer_cards) < 2:
  random_card = computer_cards.append(random.choice(cards))
 # Tính điểm 
computer_score = 0
for score in computer_cards:
  computer_score += score
print(f"Computer first's card {computer_cards[0]}")
# print(computer_cards, computer_score)

# TODO 2: Bên nào có A + A hoặc A + 10 thì win luôn, nếu không chuyển sang bước 3


# Hàm so sánh điểm
def compare_score(player_score, compare_score):
  if player_score <= 21 and player_score > computer_score:
    print(f"You win. {player_score} > {computer_score}")
  elif player_score > 21 or (player_score < computer_score and compare_score <= 21):
    print(f"You loose. {player_score} < {computer_score}")
  else:
    print(f"DraW {player_score} = {computer_score}")


# TODO 3: Nếu chưa blackjack win thì kiểm tra.
# 3.1 Nếu score trên 16 có thể giằng hoặc bốc tiếp card tối đa 3 cards [tổng 5 cards].

# 3.2: Nếu socre < 16 sẽ bốc card, nếu chưa đủ 16 bốc tiếp. Nếu score > 16 và score <= 21 quay về bước 3.1

# 3.3: Nếu score > 21 thì thua Loose.

get_card = True
while get_card:
  choice = input("Type 'y' to get another card. Type 'n' to pass: ")
  if  choice == "n" or len(player_cards) > 5 or len(computer_cards) > 5:
    # compare_score(player_score, computer_score)
    get_card = False


  if choice == 'y' and score < 16:
    pick_card = random.choice(cards)
    player_score += pick_card
    player_cards.append(pick_card)
    print(f"Your card {player_cards}. New score {player_score}")
  

  # TODO 4: Nếu cả 2 đều trên 16 và dưới 21 thì so điểm. Bên nào cao hơn sẽ win.
  compare_score(player_score, computer_score)  




  
  

    
      
    