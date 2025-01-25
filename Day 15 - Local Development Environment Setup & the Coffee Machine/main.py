"""
    The COFFEE Machine    
"""
MENU = {
    'espresso' : {
        'ingredients' : {
            'water': 50,
            'coffee':18,
        },
        'cost' : 1.5
    },
    'latte' : {
        'ingredients' : {
            'water': 200,
            'coffee':24,
            'milk':150,
        },
        'cost' : 2.5
    },
    'cappuccino' : {
        'ingredients' : {
            'water': 250,
            'coffee':24,
            'milk':100,
        },
        'cost' : 3.0
    }
}
COINS = {
    'quarters' : 25,
    'dimes' : 10,
    'nickles' : 5,
    'pennies' : 1,
}
COINS_LIST = ['quarters',
    'dimes',
    'nickles',
    'pennies']

resourcese = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}



# Functions
def print_report ():
    print(f'Water: {resourcese['water']}ml\nMilk: {resourcese['milk']}ml\nCoffee: {resourcese['coffee']}g\nMoney: ${resourcese['money']}')

def check_enough_resources(order_ing):
    for k in order_ing.keys():
        if order_ing[k] > resourcese[k]:
            print(f'Sorry there is not enough {k}')
            return False
        
    return True

def check_enough_payment(orderCost, customerPayment):
    moneyPaied = 0
    for k in customerPayment:
        moneyPaied += customerPayment[k] * COINS[k]
    costInCents= orderCost * 100
    change = moneyPaied - costInCents
    if change < 0:
        print("Sorry that's not enough money, Money Refunded.")
        return False
    if change > 0 :
        print(f"Here is ${change/100} in change")
    return True

def modify_resources(order):
    for k in order["ingredients"].keys():
        resourcese[k] -= order["ingredients"][k]
    resourcese["money"] += order["cost"]
    

while True:
    payment = {
}
    # TODO: Ask For Order Prompt 
    order = input('What would you Like to Order ? (latte/cappuccino/espresao) : ')
    # TODO: Print Report if input is report
    if (order == 'report'):
        print_report()
        continue
    # TODO: End Programme if input is off 
    if (order == 'off'):
        print("Goodbye")
        break
    # TODO: Check if there is enough Resources 
    chosenOrder = MENU[order]
    if not (check_enough_resources(chosenOrder['ingredients'])):
        continue
    # TODO: Process Coins
    print("Please Insert Coins")
    for coin in COINS_LIST:
        payment[coin] = int(input(f'How many {coin}?: '))
    if not check_enough_payment(chosenOrder['cost'], payment) :
        continue
    # TODO: Handle Order 
    print(f'Here is Your {order}, Enjoy')
    # TODO: Modefiey Resources
    modify_resources(chosenOrder)
