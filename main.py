from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True
while is_on:
    choice = input(f"Hello I'm the Coffee Machine!\nWhat would you like to drink?{menu.get_items()}:")
    if choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice.lower() == "off":
        print("Coffee Machine has been turned off!")
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
