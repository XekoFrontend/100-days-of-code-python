target = int(input("Enter a number between 0 and 1000: "))

target = target + 1

if target == 100:
  numbers = range(2,target, 2)
elif 0 <= target <= 1000: # Don't need anymore because 0 + 0 = 0. Just simply set star = 2
  numbers = range(0,target, 2)
else:
  print("Out of range")
  numbers = []

total = 0
for number in numbers:
  total += number
  
print(f"Total = {total}")


# Angela's code solution
# even_sum = 0
# for number in range(2, target + 1, 2):
#   even_sum += number
# print(even_sum)