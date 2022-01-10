from data import MENU, resources

resources_remaining = resources.copy()
user_change = {}
money = [0]


# TODO: Print Report
def print_report(resource_remaining, money_in_machine):
    for k, v in resource_remaining.items():
        if k == "water" or k == "milk":
            print(f"{k.title()}: {v}ml")
        else:
            print(f"{k.title()}: {v}g")
    print(f"Money: ${money_in_machine}")


# TODO: Check resources sufficient?
def check_resources(drink):
    resources_required = MENU[drink]["ingredients"]
    for k, v in resources_required.items():
        if v > resources_remaining[k]:
            return k
    for k, v in resources_required.items():
        resources_remaining[k] -= v
    return 2


# TODO: Process coins
# TODO: Check transaction successful?
def process_coins(drink):
    print("Please insert coins.")
    user_change["quarters"] = int(input("how many quarters?: "))
    user_change["dimes"] = int(input("how many dimes?: "))
    user_change["nickles"] = int(input("how many nickles?: "))
    user_change["pennies"] = int(input("how many pennies?: "))
    total_change = user_change["quarters"] * 0.25 + user_change["dimes"] * 0.10 + user_change["nickles"] * 0.05 + \
                   user_change["pennies"] * 0.01
    if total_change >= MENU[drink]["cost"]:
        change_return = round(total_change - MENU[drink]["cost"], 2)
        print(f"Here is ${change_return} in change.")
        money[0] += round(MENU[drink]["cost"], 2)
        return 1
    print("Sorry that's not enough money. Money refunded.")
    return 0


# TODO: Make Coffee
def make_coffee(drink):

    print(f"Here is your {drink} ☕️. Enjoy!")


while True:
    response = input("  What would you like? (espresso/latte/cappuccino): ")
    if response == "off":
        machineON = False
        break
    elif response == "report":
        print_report(resources_remaining, money[0])
    else:
        missingResource = check_resources(response)
        if missingResource != 2:
            print(f"Sorry there is not enough {missingResource}.")
        elif process_coins(response) == 0:
            continue
        else:
            make_coffee(response)

