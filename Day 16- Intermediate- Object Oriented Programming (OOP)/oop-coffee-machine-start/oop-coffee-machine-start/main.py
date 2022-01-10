from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()

while True:
    response = input(f"What would you like? ({menu.get_items()}): ")

    if response == "off":
        break
    elif response == "report":
        coffeemaker.report()
        money.report()
    else:
        order = menu.find_drink(response)

        if coffeemaker.is_resource_sufficient(order):
            if money.make_payment(order.cost):
                coffeemaker.make_coffee(order)
