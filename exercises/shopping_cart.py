class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def total_price(self):
        return sum(item["price"] for item in self.items)

cart = ShoppingCart()
cart.add_item("Book", 10)
cart.add_item("Pen", 2)
print("Total:", cart.total_price())
