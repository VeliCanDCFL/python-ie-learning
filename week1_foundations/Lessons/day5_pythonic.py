numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic loop way
squares = []
for n in numbers:
    squares.append(n ** 2)

# List comprehension — same thing in one line
squares = [n ** 2 for n in numbers]

# With a condition
evens = [n for n in numbers if n % 2 == 0]

# Combining both — squares of even numbers only
even_squares = [n ** 2 for n in numbers if n % 2 == 0]

print(squares)
print(evens)
print(even_squares)

# Real IE example — filter out defective products
products = [
    {"name": "Bolt", "defect_rate": 0.02},
    {"name": "Plate", "defect_rate": 0.08},
    {"name": "Rod", "defect_rate": 0.01},
    {"name": "Gear", "defect_rate": 0.12},
]

# Get names of products with defect rate above 5%
defective = [p["name"] for p in products if p["defect_rate"] > 0.05]
print(f"Defective products: {defective}")

print("-"*40)

# Basic dict comprehension
workers = ["Ali", "Sara", "John", "Lena"]
productivity = [120, 95, 110, 130]

# Zip two lists into a dictionary
worker_productivity = {w: p for w, p in zip(workers, productivity)}
print(worker_productivity)

# Filter — only workers above 100 units
high_performers = {w: p for w, p in worker_productivity.items() if p > 100}
print(f"High performers: {high_performers}")

# Transform values — convert to percentage of max
max_prod = max(worker_productivity.values())
performance_pct = {w: round(p / max_prod * 100, 1) for w, p in worker_productivity.items()}
print(f"Performance %: {performance_pct}")

print("-"*40)

# *args — any number of positional arguments
def calculate_total(*args):
    return sum(args)

print(calculate_total(10, 20, 30))
print(calculate_total(5, 15))
print(calculate_total(1, 2, 3, 4, 5, 6))

# **kwargs — any number of keyword arguments
def machine_report(**kwargs):
    print("--- Machine Report ---")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

machine_report(name="CNC Lathe", speed=1500, status="running", temp=72.5)

# Combining both
def production_summary(factory_name, *products, **stats):
    print(f"\nFactory: {factory_name}")
    print(f"Products: {', '.join(products)}")
    for stat, value in stats.items():
        print(f"  {stat}: {value}")

production_summary(
    "Istanbul Plant",
    "Steel Bolt", "Aluminum Plate", "Titanium Rod",
    total_units=850,
    efficiency=0.92,
    defect_rate=0.03
)

print("-"*40)

# Regular function vs lambda
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))

# Real power — using lambda with sorted()
workers = [
    {"name": "Ali", "units": 120, "department": "Production"},
    {"name": "Sara", "units": 95, "department": "Quality"},
    {"name": "John", "units": 110, "department": "Production"},
    {"name": "Lena", "units": 130, "department": "Logistics"},
]

# Sort by units
by_units = sorted(workers, key=lambda w: w["units"], reverse=True)
for w in by_units:
    print(f"{w['name']}: {w['units']} units")

print("---")

# map() — apply a function to every item
units = [120, 95, 110, 130]
bonuses = list(map(lambda u: round(u * 0.1, 2), units))
print(f"Bonuses: {bonuses}")

# filter() — keep items that match a condition
high_performers = list(filter(lambda w: w["units"] > 100, workers))
print(f"High performers: {[w['name'] for w in high_performers]}")

print("-"*40)

# Without type hints
def calculate_efficiency(produced, target):
    return produced / target * 100

# With type hints
def calculate_efficiency(produced: int, target: int) -> float:
    return produced / target * 100

# Complex type hints
from typing import Optional

def find_worker(name: str, workers: list[dict]) -> Optional[dict]:
    for worker in workers:
        if worker["name"] == name:
            return worker
    return None   # Optional means it can return None

def batch_discount(prices: list[float], discount: float = 0.10) -> list[float]:
    return [round(p * (1 - discount), 2) for p in prices]


# Test them
workers = [
    {"name": "Ali", "units": 120},
    {"name": "Sara", "units": 95},
]

efficiency = calculate_efficiency(450, 500)
print(f"Efficiency: {efficiency}%")

worker = find_worker("Ali", workers)
print(f"Found: {worker}")

missing = find_worker("John", workers)
print(f"Missing: {missing}")

prices = [2.5, 15.0, 80.0]
discounted = batch_discount(prices)
print(f"Discounted: {discounted}")

print("-"*40)

from dataclasses import dataclass
from typing import Optional

@dataclass
class ProductionRecord:
    worker: str
    units: int
    defects: int
    shift: str

    @property
    def defect_rate(self) -> float:
        return round(self.defects / self.units * 100, 2)

    @property
    def net_units(self) -> int:
        return self.units - self.defects

    def __str__(self) -> str:
        return f"{self.worker} | Net: {self.net_units} | Defect rate: {self.defect_rate}%"


def analyze_shift(records: list[ProductionRecord], shift: str) -> dict:
    shift_records = [r for r in records if r.shift == shift]
    
    if not shift_records:
        return {}

    total_units = sum(r.net_units for r in shift_records)
    avg_defect = round(sum(r.defect_rate for r in shift_records) / len(shift_records), 2)
    best_worker = max(shift_records, key=lambda r: r.net_units)

    return {
        "shift": shift,
        "total_units": total_units,
        "avg_defect_rate": avg_defect,
        "best_worker": best_worker.worker
    }


records = [
    ProductionRecord("Ali", 120, 3, "Morning"),
    ProductionRecord("Sara", 95, 5, "Morning"),
    ProductionRecord("John", 110, 2, "Evening"),
    ProductionRecord("Lena", 130, 4, "Evening"),
]

# Print all records
for r in records:
    print(r)

print("-"*20)

# Analyze each shift
for shift in ["Morning", "Evening"]:
    stats = analyze_shift(records, shift)
    print(f"{stats['shift']} shift | Total: {stats['total_units']} units | "
          f"Avg defect: {stats['avg_defect_rate']}% | Best: {stats['best_worker']}")