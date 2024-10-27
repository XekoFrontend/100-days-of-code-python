import string
alphabet = list(string.ascii_lowercase)
shift = int(input("Enter a testing number: "))

checkpoint = (len(alphabet) -1) # checkpoint = 25
if shift > checkpoint:
  while shift > checkpoint:    
    shift -= checkpoint
    if shift < checkpoint:
      break    
  print(f"\nThe langer number has been processed: {shift}")
elif shift <= checkpoint and shift > 0:
  print(f"\nThe number smaller or equal checkpoint: {shift}")
else:
  print("The number should be langer than zero!")

# Print testing
# print(f"length: {len(alphabet)}")
# print(f"Checkpoint: {checkpoint}")
# print(f"index of the latest letter (z): {alphabet.index("z")}")
