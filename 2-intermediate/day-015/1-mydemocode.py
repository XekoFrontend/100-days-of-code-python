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
    """ Kiểm tra nếu nguyên liệu trong kho có đủ làm đồ uống cho khách không?"""
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry there is not enough {item}.")
            # We're going to return False because there is not enough resources.
            return False
    # If the loop completes without returning False, return True.
    return True

def process_coins():
    """ Returns the total calculated from coins inserted. """
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

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
            print(f"{i}: {resource[i]} ml")
        print(f"Money: {profit} $")
    # TODO 4:
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if is_resource_sufficient(order_ingredients=drink["ingredients"]):
            payment = process_coins()
    else:
        print("Please spell correctly: espresso/latte/cappuccino/report/off")


  