import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(best_buy):
    """Starts the store interface."""
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print()
        try:
            choice = int(input("Please choose a number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            for product in best_buy.get_all_products():
                print(product.show())
        elif choice == 2:
            print(best_buy.get_total_quantity())
        elif choice == 3:
            active_products = best_buy.get_all_products()
            print("------")
            for index, product in enumerate(active_products, 1):
                print(f"{index}. ", end="")
                print(product.show())
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            while True:
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break

                amount_choice = input("What amount do you want? ")

                if amount_choice == "":
                    break

                try:
                    shopping_list.append((active_products[int(product_choice) - 1], int(amount_choice)))
                    print("Product added to list!")
                except ValueError:
                    print("Product not added to the list, try again")
                    continue

            print("********")
            total = best_buy.order(shopping_list)
            print(f"Order made! Total payment: ${total}")
            print()
        elif choice == 4:
            break
        else:
            print("Choice has to be 1, 2, 3 or 4")


if __name__ == "__main__":
    start(best_buy)