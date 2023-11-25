# COFFEE MACHINE CODE v0.1
from art import logo
import os
import time

# Define the menu with available drinks and their ingredients/cost
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

# Initialize profit and available resources
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True if the order can be made; or False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"\nSorry, not enough {item}.\n")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins\n")
    total = int(input("How many quarters?:  ")) * 0.25
    total += int(input("How many dimes?:  ")) * 0.1
    total += int(input("How many nickels?:  ")) * 0.05
    total += int(input("How many pennies?:  ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is successful; or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is your ${change} in change.\n")
        global profit
        profit += drink_cost
        return True
    else:
        print("\nSorry, insufficient coins.\n")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️☕️\n")

# Main program loop
print(logo)
is_on = True
while is_on:
    # User input for drink choice
    choice = input("What would you like? (Cappuccino/ Espresso/ Latte):   ").lower()
    if choice == 'off':
        # Turn off the machine
        is_on = False
        print("\nMachine TURNED OFF\nThank you for buying COFFEE 🤩\n")
        time.sleep(5)
        os.system('clear' if os.name == 'posix' else 'cls')
    elif choice == 'report':
        # Display a report of available resources
        print(f"Water = {resources['water']} ml")
        print(f"Milk = {resources['milk']} ml")
        print(f"Coffee = {resources['coffee']} g")
        print(f"Money = $ {profit}\n")
    else:
        # Process user's drink choice
        drink = MENU.get(choice)
        if drink and is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# Final message after turning off the machine
time.sleep(5)
os.system('clear' if os.name == 'posix' else 'cls')

# END OF CODE ##############################################################
