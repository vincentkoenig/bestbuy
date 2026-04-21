import products

class Store:
    """Represents a store with a list of products."""

    def __init__(self, product):
        """Initializes the store with a list of products."""
        self.product = product

    def add_product(self, product):
        """Adds a product to the store."""
        self.product.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.product.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of all products in the store."""
        total_quantity = 0
        for product in self.product:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Returns a list of all active products in the store."""
        all_products = []
        for product in self.product:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        """Buys a list of products and returns the total price."""
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