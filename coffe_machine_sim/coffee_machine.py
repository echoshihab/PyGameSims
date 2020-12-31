'''My Solution to Day 15 - > Coffee Machine from 100 days of Code by Dr. Angela'''
from decimal import Decimal

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(item_ingredients, machine_resources):
    for key in item_ingredients.keys():
        if item_ingredients[key] > machine_resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def check_transaction(total_paid, item_cost):
    if total_paid < item_cost:
        print(f"Sorry there is not enough money. Money Refunded")
        return False
    return True


def modify_resources(item_ingredients, item_cost, machine_resources):
    for key in item_ingredients.keys():
        machine_resources[key] = machine_resources[key] - item_ingredients[key]
    current_money = resources.get("money", 0)
    current_money += item_cost
    machine_resources["money"] = current_money
    return machine_resources


def return_cash(total, item_cost):
    if total > item_cost:
        return_amount = Decimal(total - item_cost).quantize(Decimal("0.01"))
        print(f"Here is ${return_amount} in change")


prompt = "on"

while prompt != "off":
    prompt = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "report":
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"Money: {resources.get('money', 0)}")
    elif prompt in MENU and check_resources(MENU[prompt]["ingredients"], resources):
        quarters = 0.25 * int(input("How many quarters:  "))
        dimes = 0.10 * int(input("How many dimes: "))
        nickels = 0.05 * int(input("How many nickels: "))
        pennies = 0.01 * int(input("How many pennies: "))
        total = quarters + dimes + nickels + pennies

        if check_transaction(total, MENU[prompt]["cost"]):
            resources = modify_resources(
                MENU[prompt]["ingredients"], MENU[prompt]["cost"], resources
            )
            return_cash(total, MENU[prompt]["cost"])

            print(f"Here is your {prompt}. Enjoy!")
    elif prompt != "off":
        print("Invalid choice, please try again")
