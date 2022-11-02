MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """ Retorna True quando o pedido pode ser feito, False se os ingredientes forem insuficientes"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Desculpe, não há {item} suficiente.")
            return False
    return True


def process_coins():
    """ Retorna o total de moedas inseridas """
    print("Insira moedas.")
    total = int(input("Quantas moedas de 1 real? ")) * 1
    total += int(input("Quantas moedas de 50 centavos? ")) * 0.5
    total += int(input("Quantas moedas de 25 centavos? ")) * 0.25
    total += int(input("Quantas moedas de 10 centavos? ")) * 0.1
    return total


def is_transaction_successful(money_received, drink_cost):
    """ Retorna True quando o pagamento for aceito, ou False se o pagamento for recusado """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aqui está R$ {change} em troco.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Desculpe, isso não é suficiente. Dinheiro devolvido.")
        return False


def make_coffee(drink_name, order_ingredients):
    """ Deduz os ingredientes do pedido do recurso """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui está seu {drink_name} ☕. Bom proveito!")


is_on = True

while is_on:
    choice = input(
        "O que você gostaria de pedir? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Água: {resources['water']}ml")
        print(f"Leite: {resources['milk']}ml")
        print(f"Café: {resources['coffee']}g")
        print(f"Dinheiro: R$ {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
