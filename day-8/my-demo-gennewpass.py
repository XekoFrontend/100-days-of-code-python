#################################
# ENCRYPTION PASSWORD EXERCISE
#################################
lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# User's input
password = input("Nhập mật khẩu của bạn: ").lower()
encrypt_choice = input("Bạn muốn mã hóa hay giải mã (e/d): ").lower()
shift = int(input("Nhập số bước: "))

# process checkpoint
checkpoint = (len(lowercase_alphabet) -1) # int = 25
while shift > checkpoint:    
    new_shift = shift - checkpoint
    if new_shift < checkpoint:
      break 

# Encryption function
def encryption_password(password, shift):
  new_pass = ""
  for letter in password:
    if letter in lowercase_alphabet:
      lowercase_index = int(lowercase_alphabet.index(letter)) + shift
      letter_shift = lowercase_alphabet[lowercase_index]
      new_pass += letter_shift
  print(new_pass)
# Check for encryption or decryption
if encrypt_choice == "e":
  encryption_password(password, shift)
elif encrypt_choice == 'd':
  decryption = 0 - shift
  encryption_password(password, decryption)



  ########### GENERATED ALPHABET LIST ###########
# The - string - module provides a simple way to generate lists of the alphabet.
'''
import string
# Lowercase alphabet
lowercase_alphabet = list(string.ascii_lowercase)
print(lowercase_alphabet)
# Lowercase alphabet
uppercase_alphabet = list(string.ascii_uppercase)
print(uppercase_alphabet)
# Both lowercase and uppercase
full_alphabet = list(string.ascii_letters)
print(full_alphabet)
'''