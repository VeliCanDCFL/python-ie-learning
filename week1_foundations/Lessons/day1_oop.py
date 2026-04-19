class Machine:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.name} started at speed {self.speed}")

    def stop(self):
        self.is_running = False
        print(f"{self.name} stopped")

    def status(self):
        state = "running" if self.is_running else "stopped"
        print(f"{self.name} is currently {state}")

# Creating objects from the blueprint
machine1 = Machine("CNC Lathe", 1500)
machine2 = Machine("Conveyor Belt", 300)


machine1.start()
machine1.status()
machine2.status()
machine1.stop()
machine1.status()

class Factory:
    
    total_machines = 0  # class attribute — shared by ALL objects
    
    def __init__(self, name):
        self.name = name  # instance attribute — unique to each object
        Factory.total_machines += 1

    def info(self):
        print(f"{self.name} | Total factories: {Factory.total_machines}")


f1 = Factory("Istanbul Plant")
f2 = Factory("Ankara Plant")
f3 = Factory("Bursa Plant")

f1.info()
f2.info()
f3.info()


class Product:
    
    def __init__(self, name, production_cost, quantity):
        self.name = name
        self.production_cost = production_cost
        self.quantity = quantity

    def total_cost(self):
        return self.production_cost * self.quantity

    def selling_price(self, margin):
        return self.production_cost * (1 + margin)

    def profit(self, margin):
        revenue = self.selling_price(margin) * self.quantity
        return revenue - self.total_cost()

    def is_profitable(self, margin):
        return self.profit(margin) > 0
        
    def __str__(self):
        return f"Product: {self.name} | Cost: ${self.production_cost} | Qty: {self.quantity}"
    
    def report(self, margin):
        print(f"--- {self.name} Report ---")
        print(f"Total cost:    ${self.total_cost():.2f}")
        print(f"Selling price: ${self.selling_price(margin):.2f}")
        print(f"Total profit:  ${self.profit(margin):.2f}")
        print(f"Profitable: {self.is_profitable(margin)}")

p1 = Product("Steel Bolt", 2.5, 1000)
p2 = Product("Aluminum Plate", 15.0, 200)

p1.report(0.30)
p2.report(0.45)

print(f"Steel Bolt is profitable: {p1.is_profitable(0.30)}")
print(f"Aluminum Plate is profitable: {p2.is_profitable(0.45)}")

print(p1)
print(p2)