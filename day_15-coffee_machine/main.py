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

money = {
    "value": 0,
}


# Show report
def show_report():
    '''Show amount of avalialabe resources'''
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money["value"]}")


# function for each coffee
def select_coffee(pay, coffee, rem_res, rem_money, name):
    '''Logic for selecting coffee and changing resources and money
    Args:
        pay(int): User input of coins
        coffee(dict): coffee menu dictionary
        rem_res(dict): resources dictionary
        rem_money(dict): money dictionary
    '''

    if pay < coffee["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = pay - coffee["cost"]
        if change > 0:
            print(f"Here is ${round(change, 2)} in change.")
        rem_money["value"] += round(pay, 2)
        rem_money["value"] = round(rem_money["value"], 2)
        coff_ing = coffee["ingredients"]

        for res in coff_ing:
            rem_res[res] -= coff_ing[res]

        print(f"Here is your {name} ☕. Enjoy!")


# Check resources are sufficient
def check_resources(ingredients, available_res):
    '''Check if enough resources are available
    Args:
        ingredients(dict): List of ingrefients for coffee
        available_res(dict): List of available resources
    Return:
        ing(str): Resource that is insufficient
        True: No resource lacking
    '''

    for ing in ingredients:
        if available_res[ing] < ingredients[ing]:
            return ing
    return True


# Calculate pay
def sum_pay():
    '''Ask and Calcalate the user's total pay'''
    print("Print insert coins.")
    quaters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quaters + dimes + nickles + pennies
    return total


running = True
while running:
    choice = input("What would you like? (espresso/latte/cappuccino): ")\
            .lower()
    match choice:
        case "espresso":
            is_sufficient = check_resources(MENU["espresso"]["ingredients"],
                                            resources)
            if is_sufficient is True:
                pay = sum_pay()
                select_coffee(pay, MENU["espresso"], resources, money,
                              "espresso")
            else:
                print(f"Sorry there is not enough {is_sufficient}")
        case "latte":
            is_sufficient = check_resources(MENU["latte"]["ingredients"],
                                            resources)
            if is_sufficient is True:
                pay = sum_pay()
                select_coffee(pay, MENU["latte"], resources, money, "latte")
            else:
                print(f"Sorry there is not enough {is_sufficient}")
        case "cappuccino":
            is_sufficient = check_resources(MENU["cappuccino"]["ingredients"],
                                            resources)
            if is_sufficient is True:
                pay = sum_pay()
                select_coffee(pay, MENU["cappuccino"], resources, money,
                              "cappuccino")
            else:
                print(f"Sorry there is not enough {is_sufficient}")
        case "report":
            show_report()
        case "off":
            running = False
