class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initializes the product with name, price and quantity."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        elif name == "":
            raise ValueError("Name cannot be empty")
        self.name = name

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a float or a integer")
        elif price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a integer")
        elif quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity

        self.active = True

    def get_quantity(self):
        """Returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        """Returns True if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns the product details."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buys a given quantity of the product and returns the total price."""
        if not self.active:
            raise ValueError("Product is not active")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()