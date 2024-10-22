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
###########
# PASSWORD EXERCISE
lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Input demo
old_pass = "abcd"
shift = int(2)
# Testing index location shift
new_pass = ""
for letter in old_pass:
  if letter in lowercase_alphabet:
    lowercase_index = int(lowercase_alphabet.index(letter)) + shift
    letter_shift = lowercase_alphabet[lowercase_index]
    new_pass += letter_shift
print(old_pass)
print(new_pass)