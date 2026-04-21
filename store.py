import products

class Store:
    def __init__(self, product):
        self.product = product

    def add_product(self, product):
        self.product.append(product)

    def remove_product(self, product):
        self.product.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        all_products = []
        for product in self.product:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        total_price = 0
        for tupel in shopping_list:
            product = tupel[0]
            quantity = tupel[1]
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))

if __name__ == "__main__":
    main()