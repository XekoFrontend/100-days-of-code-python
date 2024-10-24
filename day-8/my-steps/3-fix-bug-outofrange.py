import string
alphabet = list(string.ascii_lowercase)
old_word = "abcxyz"
shift = 37 # Need to be <= 26 (number_alphabet)
if shift > len(alphabet):
  while shift > 26 :    
    shift -= len(alphabet)
    if shift <= 26:
      break    
  print(f"while {shift}")
else:
  print(shift)

# new_word = ""
# number_alphabet = len(alphabet)

# for letter in old_word:
#   if letter in alphabet:
#     shift_index = alphabet.index(letter) + shift
#     if shift_index < number_alphabet:
#       new_word += alphabet[shift_index]
#     else:
#       negative_index = shift_index - number_alphabet    
#       new_word +=alphabet[negative_index]

# print(new_word)



# import string
# alphabet = list(string.ascii_lowercase)
# old_word = "abcxyz"
# shift = 13 # Need to be <= 26 (number_alphabet)
# new_word = ""
# number_alphabet = len(alphabet)

# for letter in old_word:
#   if letter in alphabet:
#     shift_index = alphabet.index(letter) + shift
#     if shift_index < number_alphabet:
#       new_word += alphabet[shift_index]
#     else:
#       negative_index = shift_index - number_alphabet    
#       new_word +=alphabet[negative_index]

# print(new_word)