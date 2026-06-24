# ByteBites Backend Models
# This file defines the core data structures for the ByteBites system.
#
# Classes:
# - Customer: Represents a user with a name and purchase history used for verification.
# - FoodItem: Represents a menu item with name, price, category, and popularity rating.
# - Menu: Stores and manages the full collection of FoodItem objects and supports filtering.
# - Transaction: Represents a customer's order, storing selected items and computing total cost.

# ByteBites Backend Models
# Core system classes: Customer, FoodItem, Menu, Transaction

# ByteBites Backend Models
# Core system classes: Customer, FoodItem, Menu, Transaction

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)

    def is_verified_user(self):
        return len(self.purchase_history) > 0


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self, customer):
        self.customer = customer
        self.selected_items = []

    def add_item(self, item):
        self.selected_items.append(item)

    def compute_total(self):
        return sum(item.price for item in self.selected_items)
    
if __name__ == "__main__":
    menu = Menu()

    burger = FoodItem("Burger", 10, "Food", 4.5)
    soda = FoodItem("Soda", 5, "Drinks", 4.0)
    cake = FoodItem("Cake", 7, "Desserts", 4.8)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    print("Drinks:", [i.name for i in menu.filter_by_category("Drinks")])
    print("Sorted:", [i.name for i in menu.sort_by_popularity()])

    t = Transaction(Customer("Abi"))
    t.add_item(burger)
    t.add_item(soda)

    print("Total:", t.compute_total())    