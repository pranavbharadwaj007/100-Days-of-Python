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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resource(drink, resource):

    if MENU[drink]["ingredients"][resource] < resources[resource]:

        return True

    else:

        return False


def check_transaction_success(drink, money):

    if MENU[drink]["cost"] <= money:

        return True

    else:

        return False


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    return total


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # Handle special cases
    if user_input == "off":
        break

    elif user_input == "report":
        print_report()
        continue

    # Handle Resources
    if not check_resource(user_input, "water"):

        print("Sorry, there is not enough water.")
        continue

    elif not check_resource(user_input, "coffee"):

        print("Sorry, there is not enough coffee.")
        continue

    elif user_input != "espresso":

        if not check_resource(user_input, "milk"):

            print("Sorry, there is not enough milk.")
            continue

    # Process Coins
    given = process_coins()

    # Check transaction success
    if not check_transaction_success(user_input, given):

        print("Sorry, that's not enough money. Money refunded.")
        continue

    else:

        cost = MENU[user_input]["cost"]
        change = given - cost
        resources["money"] += cost

        print(f"Here is ${round(change, 2)} dollars in change")

    # Make drink
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]

    if user_input != "espresso":

        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]

    print(f"Here is your {user_input}. Enjoy!")
