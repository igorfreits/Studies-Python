class CartValue:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.name, product.value)

    def soma_total(self):
        total = 0
        for product in self.products:
            total += product.value
        return total


class Produto:
    def __init__(self, name, value):
        self.name = name
        self.value = value
