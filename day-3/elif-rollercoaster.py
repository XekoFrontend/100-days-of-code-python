"""
Flow Chart link:
https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D
"""

print("*** Welcome to the Rollercoaster! ***")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
  age = int(input("How old are you?\n"))
  if age < 12:
    bill = 5
    print('Kid tickets cost $5.')
  elif age <= 18:
    bill = 7
    print("Teen tickets cost $12.")
  elif age >= 45 and age <= 55: #45 <= age <= 55
    bill = 0
    print(f"Older tickets cost ${bill}")
  else:
    bill = 12
    print("Adult tickets cost $7.")
  # Ticketing version
  extra_photo = input("Do you want to take a photo? y or n\n")

  if extra_photo == "y":
    bill += 3
    # print(f"Your bill is ${bill}")  
  print(f"Your bill is ${bill}")

else:
  print("You can't ride 😒")



"""
Ticketing flow chart version
https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload
"""