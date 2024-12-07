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

# TODO 1:  Prompt user by asking
user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
turn_of_marchine = False
while not turn_of_marchine:
  user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if user_input == "espresso":
    print(MENU["espresso"])
  elif user_input == "latte":
    print(MENU["latte"])
  elif user_input == "cappuccino":
    print(MENU["cappuccino"])
  elif user_input == "off":
    turn_of_marchine = True
  else:
    print("Please spell correctly: espresso/latte/cappuccino")
