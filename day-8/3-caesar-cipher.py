import string
alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' or 'decode':\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
  output_text = ""
  for letter in original_text:
    if encode_or_decode == "decode":
      shift_amount *= -1
    shifted_position = alphabet.index(letter) + shift_amount # ex: 25 + 9 = 34      
    shifted_position %= len(alphabet)                        # ex: 34 % 25 = 9
    output_text += alphabet[shifted_position]
  print(output_text)

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)