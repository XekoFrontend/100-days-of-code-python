import random

# My code is not effective.
# random_float = random.random() * 2
# coin_toss = int(random_float)

# if coin_toss == 0:
#   print("Tails")
# elif coin_toss == 1:
#   print("Heads")

# Angela's code solution
coin_toss = random.randint(0,1)

if coin_toss == 0:
  print("Tails")
elif coin_toss == 1:
  print("Heads")