from dataclasses import dataclass, asdict
from typing import Optional
import json


class ProductNotFoundError(Exception):
    def __init__(self, product_id: str):
        super().__init__(f"Product '{product_id}' not found in inventory.")

class DuplicateProductError(Exception):
    def __init__(self, product_id: str):
        super().__init__(f"Product '{product_id}' already exists.")

class InvalidQuantityError(Exception):
    def __init__(self, quantity: int):
        super().__init__(f"Invalid quantity: {quantity}. Must be greater than 0.")


@dataclass
class Product:
    product_id: str
    name: str
    price: float
    quantity: int

    @property
    def total_value(self) -> float:
        return round(self.price * self.quantity, 2)

    def __str__(self) -> str:
        return (f"{self.product_id} | {self.name} | "
                f"${self.price} | Qty: {self.quantity} | "
                f"Value: ${self.total_value}")


class Inventory:
    def __init__(self, filepath: str = "inventory.json"):
        self.filepath = filepath
        self.products: dict[str, Product] = {}
        self.load()

    def add(self, product_id: str, name: str, price: float, quantity: int) -> None:
        if quantity <= 0:
            raise InvalidQuantityError(quantity)
        if product_id in self.products:
            raise DuplicateProductError(product_id)
        self.products[product_id] = Product(product_id, name, price, quantity)
        self.save()
        print(f"Added: {name}")

    def remove(self, product_id: str) -> None:
        if product_id not in self.products:
            raise ProductNotFoundError(product_id)
        name = self.products[product_id].name
        del self.products[product_id]
        self.save()
        print(f"Removed: {name}")

    def update(self, product_id: str, quantity: int) -> None:
        if product_id not in self.products:
            raise ProductNotFoundError(product_id)
        if quantity <= 0:
            raise InvalidQuantityError(quantity)
        self.products[product_id].quantity = quantity
        self.save()
        print(f"Updated quantity for {self.products[product_id].name} to {quantity}")

    def report(self) -> None:
        if not self.products:
            print("Inventory is empty.")
            return
        print("\n--- Inventory Report ---")
        for product in self.products.values():
            print(product)
        total = sum(p.total_value for p in self.products.values())
        print(f"Total inventory value: ${round(total, 2)}")
        print("------------------------\n")

    def save(self) -> None:
        with open(self.filepath, "w") as f:
            json.dump([asdict(p) for p in self.products.values()], f, indent=4)

    def load(self) -> None:
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.products = {p["product_id"]: Product(**p) for p in data}
        except FileNotFoundError:
            self.products = {}