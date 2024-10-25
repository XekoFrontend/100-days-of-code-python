#################################
# ENCRYPTION PASSWORD EXERCISE
#################################
lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# User's input
password = input("Nhập mật khẩu của bạn: ").lower()
shift = int(input("Nhập số bước: "))
choice = input("Bạn muốn mã hóa hay giải mã (e/d): ").lower()
checkpoint = len(lowercase_alphabet) # checkpoint = 26

def encryption_password(password, shift, choice):
  new_pass = ""
  for letter in password:
    if letter in lowercase_alphabet:
      if choice == "e":
        lowercase_index = int(lowercase_alphabet.index(letter)) + shift
      if choice == "d":
        lowercase_index = int(lowercase_alphabet.index(letter)) - shift
      while lowercase_index > checkpoint or lowercase_index == checkpoint:
          lowercase_index -= checkpoint
      letter_shift = lowercase_alphabet[lowercase_index]
      new_pass += letter_shift      
  print(new_pass)

encryption_password(password, shift, choice)















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