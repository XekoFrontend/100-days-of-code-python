print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# Quick testing
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"

combine_name = name1.lower() + name2.lower()

count_t = combine_name.count('t')
count_r = combine_name.count('r')
count_u = combine_name.count('u')
count_e = combine_name.count('e')
count_true = count_t + count_r + count_u + count_e

count_l = combine_name.count('l')
count_o = combine_name.count('o')
count_v = combine_name.count('v')
count_e = combine_name.count('e')
count_love = count_l + count_o + count_v + count_e

true_love_total = str(count_true) + str(count_love)
score = int(true_love_total)
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos."
)
elif 40 <= score <= 50:
  print(f"Your score is {score}, you are alright together."
)
else:
  print(f"Your score is {score}.")














# lower_name1 = name1.lower()
# lower_name2 = name2.lower()

# count_letter1 = lower_name1 and lower_name2.count('t')
# count_letter1 = lower_name1.lower_name2.count('r')
# count_letter2 = lower_name2.count('u')


# length = len(count_letter)
# print(count_letter1)
# print(count_letter2)
# print(length)
# print(lower_name1)