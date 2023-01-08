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
}

# TODO:
#  1. input prompt to choose latte, cappuccino, or espresso -
#  if "off" - return to end function
#  if "report" - print out remaining ingredients and their quantities
#  1a. check_ingredients function to ensure there's enough for chosen drink. if not, print out
#  limiting ingredient and apology.
#  2. print "Please insert coins."
#  3. int(input("How many quarters?: "))
#  4. int(input("How many dimes?: "))
#  5. int(input("How many nickels?: "))
#  6. int(input("How many pennies?: "))
#  7. calculate_change function for adding money and subtracting drink cost. add drink cost to money total.
#  if drink cost > money total, print("Sorry that's not enough money.")
#  print("Money refunded.")
#  8. print(f"Here is ${change} in change.") rounded to two decimal places.
#  8a. ingredients_left function to subtract ingredient amounts from starting quantities.
#  9. print(f"Here is your {choice_drink} ☕️. Enjoy!")
#  10. repeat input prompt to choose latte, cappuccino, or espresso


def check_ingredients(choice):
    subdict = MENU[choice]["ingredients"]
    enough_ingredients = True
    for ingredient, quantity in subdict.items():
        if quantity > resources[ingredient]:
            enough_ingredients = False
            print(f"Sorry, there isn't enough {ingredient}")
    return enough_ingredients


def ingredients_left(choice):
    subdict = MENU[choice]["ingredients"]
    for ingredient, quantity in subdict.items():
        resources[ingredient] -= quantity


def calculate_change(choice, quarters, dimes, nickels, pennies):
    key_lookup = "money"
    choice_cost = MENU[choice]["cost"]
    money_sum = quarters * 0.25 + nickels * 0.05 + dimes * 0.10 + pennies * 0.01
    if money_sum < choice_cost:
        print(f"Sorry, that's an insufficient amount of money. Money refunded.")
        return False
    else:
        change = round(money_sum - choice_cost, 2)
        print(f"Here is your change: ${change}")
        if key_lookup in resources:
            resources[key_lookup] += choice_cost
        else:
            resources[key_lookup] = choice_cost
        return True


def coffee_machine():
    loop_boolean = True
    while loop_boolean:
        choice = input("What would you like? (latte, cappuccino, or espresso): ")
        key_lookup = "money"
        if choice == "off":
            loop_boolean = False
            return
        elif choice == "report":
            print(f'Water: {resources["water"]} ml')
            print(f'Milk: {resources["milk"]} ml')
            print(f'Coffee: {resources["coffee"]} g')
            if key_lookup in resources:
                print(f'Money: ${resources["money"]}')
        else:
            if check_ingredients(choice):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                enough_money = calculate_change(choice, quarters, dimes, nickels, pennies)
                if enough_money:
                    ingredients_left(choice)
                    print(f"Here is your {choice} ☕️. Enjoy!")
                elif not enough_money:
                    print("Sorry, that's not enough money.")


coffee_machine()

