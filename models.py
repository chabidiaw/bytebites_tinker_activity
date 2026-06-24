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

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

class Menu:
    def __init__(self):
        self.items = []

class Transaction:
    def __init__(self, customer):
        self.customer = customer
        self.selected_items = []