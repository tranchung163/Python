from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
is_ordering = True
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()




while is_ordering:
    options = input(f"What would you like to drink {MENU.get_items().lower()}: ")

    if options == "off":
        is_ordering = False

    elif options == "report":
        coffe_maker.report()
        money_machine.report()

    else:
        drink = MENU.find_drink(options)

        if coffe_maker.is_resource_sufficient(drink) and money_machine.process_coins:
            money_machine.make_payment(drink.cost)
            coffe_maker.make_coffee(drink)
        else:
            is_ordering = False

