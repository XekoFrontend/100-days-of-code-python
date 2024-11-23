name1 = input("The first name is: ").lower()
name2 = input("The second name is: ").lower()

def calculate_love_score(name1, name2):
  both_name = name1.lower() + name2.lower()
  true = "true"
  love = "love"
  true_score = 0
  love_score = 0
  for letter in both_name:    
    if letter in true:
      true_score += 1
    if letter in love:
      love_score += 1
  score = str(true_score) + str(love_score)
  print(score)

calculate_love_score("Angela Yu", "Jack Bauer")
### Testing
# calculate_love_score("Angela Yu", "Jack Bauer") #53
# calculate_love_score("Kanye West", "Kim Kardashian") #42