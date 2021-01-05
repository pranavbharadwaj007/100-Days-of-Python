from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while True:
    usr_ipt = input(f"What would you like? ({menu.get_items()}): ")

    if usr_ipt == "report":
        coffee.report()
        money.report()
        continue

    elif usr_ipt == "off":
        break

    else:

        order = menu.find_drink(usr_ipt)

        if coffee.is_resource_sufficient(order):

            if money.make_payment(order.cost):

                coffee.make_coffee(order)


