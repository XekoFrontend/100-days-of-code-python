"""
Flow Chart link:
https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D
"""

print("*** Welcome to the Rollercoaster! ***")
height = int(input("What is your height in cm?\n"))

if height > 120:
  age = int(input("How old are you?\n"))
  if age < 12:
    print('Your ticket costs $5.')
  elif age > 18:
    print("Your ticket costs $12.")
  else:
    print("Your ticket costs $7.")
else:
  print("You can't ride 😒")
