import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store):
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = int(input("Please choose a number: "))

        if choice == 1:
            for product in store.get_all_products():
                product.show()
        elif choice == 2:
            print(store.get_total_quantity())
        elif choice == 3:
            pass
        else:
            break


if __name__ == "__main__":
    start(best_buy)