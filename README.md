# ByteBites Tinker Activity

## Project Overview

ByteBites is a simplified backend system for a campus food ordering application. The project uses object-oriented programming in Python to model customers, food items, menus, and transactions.

## Features

* Manage customers and purchase history
* Store food item information (name, price, category, popularity rating)
* Maintain a menu of available items
* Filter menu items by category
* Create transactions and compute order totals

## Project Structure

* `bytebites_spec.md` – Client feature request and candidate classes
* `draft_from_copilot.md` – Initial AI-generated UML diagram
* `bytebites_design.md` – Final UML design
* `ByteBites_Design_Reference.md` – AI behavioral instructions
* `models.py` – Python class implementations
* `test_bytebites.py` – Automated tests
* `reflection.md` – Reflection on debugging and AI collaboration

## Demo Walkthrough

Example workflow:

1. Create a `Customer`.
2. Create several `FoodItem` objects.
3. Add items to a `Menu`.
4. Filter menu items by category.
5. Create a `Transaction`.
6. Add selected items to the transaction.
7. Compute the total cost.

## Test Output

Run the test suite with:

```bash
python -m pytest
```

All tests should pass successfully.
