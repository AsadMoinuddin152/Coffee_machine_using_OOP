from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_off = False
items = 595
while not is_off:
    options = menu.get_items()
    user_input = input(f"What would you like? {options} : ").lower()
    if user_input == "off":
        is_off = True
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            coffee_maker.report()
            money_machine.report()


