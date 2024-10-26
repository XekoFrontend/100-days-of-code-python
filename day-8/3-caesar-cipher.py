import string
alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' or 'decode':\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
  cipher_text = ""
  for letter in original_text:
    shifted_position = alphabet.index(letter) + shift_amount # ex: 25 + 9 = 34
    shifted_position %= len(alphabet)                        # ex: 34 % 25 = 9
    cipher_text += alphabet[shifted_position]
  print(cipher_text)

encrypt(original_text=text, shift_amount=shift)