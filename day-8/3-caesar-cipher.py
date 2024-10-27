import string
alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' or 'decode':\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
  output_text = ""
  # Check if the direction input is 'decode'.
  # If it is, multiply by -1; otherwise, run the encode program below.
  if encode_or_decode == "decode":
    shift_amount *= -1
  # The encode program.
  for letter in original_text:
    if letter in alphabet:   
      shifted_position = alphabet.index(letter) + shift_amount # ex: 25 + 9 = 34      
      shifted_position %= len(alphabet)                        # ex: 34 % 25 = 9
      output_text += alphabet[shifted_position]
    else:
      output_text += letter
  print(f"Here is {encode_or_decode}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)