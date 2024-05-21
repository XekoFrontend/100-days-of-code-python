# Flow Chart: https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

step1 = input("Do you want to turn left or right?\n L or R: ").upper()
if step1 == 'L':
  step2 = input("Do you want to turn swim or wait?\n S or W: ").upper()
  if step2 == "W":
    step3 = input("Which door do you want to enter. Red, Blue or Yellow?\n R, B or Y: ").upper()
    if step3 == "B":
      print("Eaten by beasts. Game Over. 💀")    
    elif step3 == "R":
      print("Burned by fire. Game Over. 💀")
    elif step3 == "Y":
      print("You Win! 🎉")
    else:
      print("Game Over. 💀")
  else:
      print("Attacked by trout. Game Over. 💀")    
else:
  print("Fall into a hole. Game Over. 💀")