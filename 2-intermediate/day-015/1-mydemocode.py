MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1:  Prompt user by asking
turn_off_machine = True
while turn_off_machine:
  choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
  # if choice == "espresso":
  #   print(MENU["espresso"])
  # elif choice == "latte":
  #   print(MENU["latte"])
  # elif choice == "cappuccino":
  #   print(MENU["cappuccino"])
  if choice == "off":
    turn_off_machine = False
  elif choice == "report":
    for i in resource:
        print(f"{i}: {resource[i]}")
  else:
    print("Please spell correctly: espresso/latte/cappuccino")


  