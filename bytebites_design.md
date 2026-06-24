# ByteBites — UML Design Diagram

```mermaid
classDiagram
    class Customer {
        -str name
        -list~Transaction~ purchase_history
        +__init__(name: str)
        +get_name() str
        +get_purchase_history() list~Transaction~
        +add_purchase(t: Transaction) None
        +is_verified_user() bool
    }

    class FoodItem {
        -str name
        -float price
        -str category
        -float popularity_rating
        +__init__(name: str, price: float, category: str, popularity_rating: float)
        +get_name() str
        +get_price() float
        +get_category() str
        +get_popularity_rating() float
    }

    class Menu {
        -list~FoodItem~ items
        +add_item(item: FoodItem) None
        +remove_item(item: FoodItem) None
        +get_items() list~FoodItem~
        +filter_by_category(category: str) list~FoodItem~
    }

    class Transaction {
        -list~FoodItem~ selected_items
        -Customer customer
        +__init__(customer: Customer)
        +add_item(item: FoodItem) None
        +get_selected_items() list~FoodItem~
        +get_customer() Customer
        +compute_total() float
    }

    Customer "1" <--> "*" Transaction : purchase history
    Menu "1" o-- "*" FoodItem : catalogs
    Transaction "*" o-- "*" FoodItem : selects
```

## Relationship Notes

- **Customer ↔ Transaction** — one bidirectional association replaces the two
  separate arrows in the draft. A `Customer` owns many `Transaction`s
  (`purchase_history`) and each `Transaction` knows its `Customer`.
- **Menu ◇— FoodItem** — aggregation: the `Menu` catalogs many `FoodItem`s, but
  items exist independently of any single menu.
- **Transaction ◇— FoodItem** — aggregation: a `FoodItem` can appear in many
  transactions, and the same item can be selected across customers (`*..*`).
