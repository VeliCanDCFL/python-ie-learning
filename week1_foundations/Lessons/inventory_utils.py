# inventory_utils.py — reusable inventory functions

class InvalidQuantityError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Invalid quantity: {quantity}. Must be greater than 0.")

class ProductNotFoundError(Exception):
    def __init__(self, product_id):
        super().__init__(f"Product '{product_id}' not found in inventory.")


def validate_order(product_id, quantity, inventory):
    if quantity <= 0:
        raise InvalidQuantityError(quantity)
    if product_id not in inventory:
        raise ProductNotFoundError(product_id)
    return True


def calculate_total(price, quantity, discount=0):
    subtotal = price * quantity
    return subtotal * (1 - discount)


INVENTORY = {
    "P001": {"name": "Steel Bolt", "price": 2.5},
    "P002": {"name": "Aluminum Plate", "price": 15.0},
    "P003": {"name": "Titanium Rod", "price": 80.0},
}