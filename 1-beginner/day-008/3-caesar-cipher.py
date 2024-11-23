import string, caesar_logo
print(caesar_logo.logo) # Create ascii arts: https://www.asciiart.eu/text-to-ascii-art
alphabet = list(string.ascii_lowercase) # Create an lowercase alphabet list from 'string' module.

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
    else: # Checking and Output non-alphabet characters.
      output_text += letter  
  print(f"Here is {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' or 'decode':\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))

  caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
  
  restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
  if restart == "no":
    print("Goodbye!🤗")
    should_continue = False    