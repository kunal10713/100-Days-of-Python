from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True

while True:
    order = input("What would you like? (espresso/latte/cappuccino/):")

    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker.report()
    else: 
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
           

        



