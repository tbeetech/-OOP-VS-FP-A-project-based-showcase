# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "milk": 300,
    "coffee": 300,
}


def process_payments(brew_type):
    default_coin_boiler = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    user_deposit_per_coin = [default_coin_boiler['quarters'],
                             default_coin_boiler['dimes'],
                             default_coin_boiler['nickles'],
                             default_coin_boiler['pennies']]

    coin_name_for_loop_print = ['quarters', 'dimes', 'nickles', 'pennies']
    count = 0

    while count < 4:
        payment_per_coin = input(f'Enter amount of {coin_name_for_loop_print[count]} to Deposit:')
        if payment_per_coin.isdigit():
            print("payment per coin is digit")
            payment_per_coin = float(payment_per_coin)
            user_deposit_per_coin[count] *= payment_per_coin
            user_deposit_per_coin[count] = round(user_deposit_per_coin[count], 2)
            count += 1
        if payment_per_coin == "report":
            report()
        if payment_per_coin == 'off':
            print('coffee machine switched off')
            exit()
    payment_summation = 0
    for each_coin_total in user_deposit_per_coin:
        payment_summation += each_coin_total

    # validate deposit and process transaction
    if payment_summation == MENU[brew_type]['cost']:
        resources['water'] -= MENU[brew_type]['ingredients']['water']
        resources['milk'] -= MENU[brew_type]['ingredients']['milk']
        resources['coffee'] -= MENU[brew_type]['ingredients']['coffee']
        print('transaction successfully processed. Thanks')

    if payment_summation > MENU[brew_type]['cost']:
        resources['water'] -= MENU[brew_type]['ingredients']['water']
        resources['milk'] -= MENU[brew_type]['ingredients']['milk']
        resources['coffee'] -= MENU[brew_type]['ingredients']['coffee']
        user_change = payment_summation - MENU[brew_type]['cost']
        print('transaction successfully processed. Thanks')
        print(f'your payment is {payment_summation} \nYour change is {user_change}')
    else:
        print(
            f'insufficient balance of :{payment_summation}\nrequired balance: {MENU[brew_type]["cost"]}')



def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")


def validate_sufficient_resources(brew_category):
    status_checker = {"coffee": None, "water": None, "milk": None}
    if MENU[brew_category] == 'espresso':
        status_checker["milk"] = True
    if resources["coffee"] < MENU[brew_category]["ingredients"]["coffee"]:
        status_checker["coffee"] = False
    else:
        status_checker["coffee"] = True
    if resources["water"] < MENU[brew_category]["ingredients"]["water"]:
        status_checker["water"] = False
    else:
        status_checker["water"] = True

    if resources["milk"] < MENU[brew_category]["ingredients"]["milk"]:
        status_checker["milk"] = False
    else:
        status_checker["milk"] = True
        status_checker["milk"] = True

    for res_status in status_checker:
        # print(each_resource)
        if not status_checker[res_status]:
            print(f"{res_status} resources not sufficient")
            break
        if status_checker[res_status]:

                print(
                    f"{res_status} resources sufficient proceed to payment for {res_status}")
                process_payments(brew_category)
                break

        if status_checker[res_status]:
            print(
                "all resources sufficient proceed to payment.")
            process_payments(brew_category)
            break


def coffee_maker():
    coffee_types_or_report = ["espresso", "latte", "cappuccino"]
    customer_coffee_choice = ""
    while customer_coffee_choice not in coffee_types_or_report:
        customer_coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
        if customer_coffee_choice == 'report':
            report()
        if customer_coffee_choice == 'off':
            print('coffee machine switched off')
            exit()
        if customer_coffee_choice in coffee_types_or_report:
            validate_sufficient_resources(customer_coffee_choice)

while True:
    coffee_maker()
