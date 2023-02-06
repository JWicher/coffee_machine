from menu import MENU
from drink_mapper import mapper_drinks
from maintenance_commands import maintenance_commands

state = {
    "turn_on": True,
    "money": 0,
    "ingradients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
}

def maintenance(command):
    """Run maintenance mode"""
    # done TODO: 1 turn off machine when input has a value of "off"
    if command == "off":
        state["turn_on"] = False

    # done TODO: 2 Print report when input has value of "report"
    elif command == "report":
        resources = state['ingradients']
        print("Report / resources:")
        print(f"    Water: {resources['water']} ml")
        print(f"    Milk: {resources['milk']} ml")
        print(f"    Coffee: {resources['coffee']} g")
        print(f"    Money: ${state['money']}")

    return


# done TODO: 3 Check resources sufficient
def check_resources(drink_name):
    """Checks if there are enough resources to prepare choosen dring"""
    drink = MENU[drink_name]
    resources = state['ingradients']

    for ingredient_name in drink["ingredients"]:
        if resources[ingredient_name] <= drink["ingredients"][ingredient_name]:
            raise Exception(f"Sorry there is not enough {ingredient_name}.")

    return drink_name

# done TODO: 4 Process coins.
# done TODO: 5 Check transaction successful?
def process_coins(choosen_drink):
    """Checks if customer put enough amount of money and returns amount of those money"""
    insterted_money = 0
    print("Insert coins:")
    insterted_money += int(input("    quarters: ")) * 0.25
    insterted_money += int(input("    dimes: ")) * 0.1
    insterted_money += int(input("    nickles: ")) * 0.05
    insterted_money += int(input("    pennies: ")) * 0.01

    if insterted_money < MENU[choosen_drink]["cost"]:
        raise Exception("Sorry that's not enough money. Money refunded.")

    return round(insterted_money)

def update_state(choosen_drink, new_coins):
    """Updates resources of the machine and money in deposit"""
    drink_ingredients = MENU[choosen_drink]["ingredients"]
    resources = state['ingradients']

    for ingradient in drink_ingredients:
        resources[ingradient] -= drink_ingredients[ingradient]

    profit = MENU[choosen_drink]["cost"]
    print(f"Here is your change!: ${new_coins - profit}")
    state["money"] += profit

    return


# done TODO: 6 Make Coffee.
def make_coffe(choosen_drink):
    """Print statement that coffe was prepared successfully"""
    print(f"Here is your {choosen_drink}. Enjoy!")


def start_machine():
    """Starts machine. Input takes values '1', '2', '3'"""
    while state["turn_on"]:
        try:
            user_choice = input("What would you like? (1: espresso / 2: latte / 3: cappuccino): ")

            if user_choice in maintenance_commands:
                maintenance(user_choice)
            else:
                mapped_drink = mapper_drinks[user_choice]
                choosen_drink = check_resources(mapped_drink)
                new_coins = process_coins(choosen_drink)
                update_state(choosen_drink, new_coins)

                make_coffe(choosen_drink)

        except Exception as e:
            print(e)

start_machine()
