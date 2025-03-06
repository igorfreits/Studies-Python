class MenuItem:
    """Modelo do menu de itens"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Modelo do menu de bebidas"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Retorna todos os itens disponíveis no menu"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Pesquisa no menu uma bebida específica pelo nome. Retorna esse item se existir, caso contrário retorna Nenhum"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
