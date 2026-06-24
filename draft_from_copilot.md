classDiagram
class Customer {
-String name
-List~Transaction~ purchaseHistory
+getName() String
+getPurchaseHistory() List~Transaction~
+addPurchase(Transaction t) void
+isVerifiedUser() boolean
}

    class FoodItem {
        -String name
        -double price
        -String category
        -double popularityRating
        +getName() String
        +getPrice() double
        +getCategory() String
        +getPopularityRating() double
    }

    class Menu {
        -List~FoodItem~ items
        +addItem(FoodItem item) void
        +removeItem(FoodItem item) void
        +getItems() List~FoodItem~
        +filterByCategory(String category) List~FoodItem~
    }

    class Transaction {
        -List~FoodItem~ selectedItems
        -Customer customer
        +addItem(FoodItem item) void
        +getSelectedItems() List~FoodItem~
        +computeTotal() double
    }

    Customer "1" --> "*" Transaction : has purchase history
    Transaction "*" --> "1" Customer : belongs to
    Menu "1" o-- "*" FoodItem : aggregates
    Transaction "1" o-- "*" FoodItem : contains
