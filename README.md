# BestBuy Store Simulator 🛒

A Python OOP project simulating a product store with inventory management, input validation, and order processing. Built to practice clean class design and object-oriented principles.

## Features

- 📦 **Product class** — create products with name, price, and quantity; auto-deactivates when stock hits zero
- 🏪 **Store class** — manages a product catalog; add/remove products, check total stock, place orders
- ✅ **Input validation** — `TypeError` and `ValueError` raised for invalid inputs throughout
- 🛍️ **Order processing** — pass a shopping list of `(product, quantity)` tuples to get the total price
- 🔒 **Active/inactive state** — products can be activated or deactivated; only active products are returned by the store

## Class Overview

```
Product
├── __init__(name, price, quantity)   # Validates all inputs on creation
├── buy(quantity)                     # Reduces stock, returns total price
├── set_quantity(quantity)            # Auto-deactivates at 0
├── is_active() / activate() / deactivate()
└── show()                            # Returns product details as string

Store
├── __init__(product_list)            # Validates list of Product instances
├── add_product(product)
├── remove_product(product)
├── get_all_products()                # Returns only active products
├── get_total_quantity()              # Sum of all stock
└── order(shopping_list)             # Processes [(product, qty), ...] tuples
```

## Project Structure

```
bestbuy/
├── products.py    # Product class
├── store.py       # Store class
└── main.py        # Demo usage
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/bestbuy.git
cd bestbuy
```

**2. Run the demo**
```bash
python store.py
```

## Example Usage

```python
from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)

# Get all active products
active = best_buy.get_all_products()

# Place an order
total = best_buy.order([(active[0], 1), (active[1], 2)])
print(f"Order total: ${total}")  # $1950.0

# Total stock
print(best_buy.get_total_quantity())  # 850
```

## What I Learned

- Designing clean, reusable classes with clear responsibilities
- Input validation with `TypeError` and `ValueError` in `__init__` methods
- Implementing automatic state management (product auto-deactivation)
- Working with lists of objects and processing them as a collection
- Separating concerns between data model (`Product`) and business logic (`Store`)
