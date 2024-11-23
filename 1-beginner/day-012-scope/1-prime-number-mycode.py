# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
def is_prime(num):
  temp_list = []
  if num < 2:
    return False
  elif num == 2:
    return True
  else:    
    for n in range(2, num):
      if num % n != 0:
        temp_list.append(True)
      else:
        temp_list.append(False)

  if False in temp_list:
    return False
  elif True in temp_list:
    return True

num = int(input("Enter a number: "))
output = is_prime(num)
print(output)




"""
NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.
Example: 73
True

Example:75
False
"""