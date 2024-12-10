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

# TODO 4: Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            # print(MENU["cost"])
            print(f"Sorry there is not enough {item}.")



profit = 0

# TODO 2: turn off machine
turn_off_machine = True
while turn_off_machine:
    # TODO 1:  Prompt user by asking
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        turn_off_machine = False
    # TODO 3:  print resource
    elif choice == "report":
        for i in resource:
            print(f"{i}: {resource[i]}")
        print(f"Money: {profit}$")
    # TODO 4:
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        is_resource_sufficient(order_ingredients=drink["ingredients"])
    else:
        print("Please spell correctly: espresso/latte/cappuccino/report/off")


  