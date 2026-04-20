# Without error handling — this crashes
# print(int("hello"))  

# With error handling
try:
    number = int("hello")
except ValueError as e:
    print(f"Error: {e}")

print("Program continues running...")

# Multiple except blocks
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers")
        return None

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "x"))

print("-"*40)

def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist")
        return None
    else:
        print(f"File read successfully")  # runs only if NO error occurred
        return content
    finally:
        print("This always runs no matter what")  # runs always


result1 = read_file("factory.json")    # exists
print("-"*40)
result2 = read_file("fake_file.txt")   # doesn't exist

print("-"*40)


class InvalidQuantityError(Exception):
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"Invalid quantity: {quantity}. Must be greater than 0.")

class ProductNotFoundError(Exception):
    def __init__(self, product_id):
        self.product_id = product_id
        super().__init__(f"Product '{product_id}' not found in inventory.")


def process_order(product_id, quantity):
    inventory = {"P001": "Steel Bolt", "P002": "Aluminum Plate"}
    
    if quantity <= 0:
        raise InvalidQuantityError(quantity)
    
    if product_id not in inventory:
        raise ProductNotFoundError(product_id)
    
    print(f"Order processed: {inventory[product_id]} x{quantity}")


# Test it
orders = [
    ("P001", 100),    # valid
    ("P001", -5),     # invalid quantity
    ("P999", 50),     # product not found
]

for product_id, quantity in orders:
    try:
        process_order(product_id, quantity)
    except InvalidQuantityError as e:
        print(f"Quantity Error: {e}")
    except ProductNotFoundError as e:
        print(f"Product Error: {e}")

print("-"*40)

from inventory_utils import validate_order, calculate_total, INVENTORY
from inventory_utils import InvalidQuantityError, ProductNotFoundError

orders = [
    ("P001", 100),
    ("P002", -5),
    ("P999", 50),
]

for product_id, quantity in orders:
    try:
        validate_order(product_id, quantity, INVENTORY)
        product = INVENTORY[product_id]
        total = calculate_total(product['price'], quantity, discount=0.10)
        print(f"Order OK: {product['name']} x{quantity} = ${total:.2f} (10% discount)")
    except InvalidQuantityError as e:
        print(f"Quantity Error: {e}")
    except ProductNotFoundError as e:
        print(f"Product Error: {e}")