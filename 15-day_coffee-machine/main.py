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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 3. Print report to see the current resources of the coffee machine
def print_report(ingredients):
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${profit}")


# TODO 4. Check if the resources are sufficient for a drink
def check_resources(order_ingredients):
    """Returns True when order can be made.
    And False if the ingredients are insufficient"""
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
        else:
            print("We have enough resources.")
            return True


# TODO 5. Process coins
def process_coins():
    """Returns the total calculated from coin inserted"""
    print("Please insert coins.")
    quarters = int(input(" How many quarters?: "))
    dimes = int(input(" How many dimes?: "))
    nickles = int(input(" How many nickles?: "))
    pennies = int(input(" How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(total)

    return total


# TODO 6. Check if the transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted.
    Return False when the payment is declined"""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True


# TODO 7. Make a coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


# TODO 1. Ask a user what they want to order
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2. Turn off the Coffee Machine by entering 'off' to the prompt
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report(resources)
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
