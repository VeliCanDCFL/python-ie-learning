#Build a factory hierarchy:

#Vehicle base class with brand, speed and methods drive() and __str__
#ElectricVehicle that inherits from Vehicle, adds battery_capacity, overrides drive() to mention it's electric
#ElectricTruck that inherits from ElectricVehicle, adds payload_tons, adds a method load() that prints how much it's carrying


class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        self.is_running = False

    def going(self):
        self.is_running = True
        print(f"{self.brand} going with {self.speed} km/h")

    def stop(self):
        self.is_running = False
        print(f"{self.brand} stopped")

    def __str__(self):
        return f"Vehicle: {self.brand} | Speed: {self.speed} km/h"
    
volvo = Vehicle("Volvo", 140)
volvo.going()
print(volvo)


class EV(Vehicle):
    
    def __init__(self, brand, speed, battery_cap):
        super().__init__(brand, speed)
        self.battery_cap = battery_cap

    def ghost(self):
        if self.is_running:
            print(f"{self.brand} has {self.battery_cap} kw battery capacity and going silently at {self.speed} km/h")
        else:
            print(f"{self.brand} is not running. Start it to drive.")

    def __str__(self):
        return f"EV: {self.brand} | Battery Capacity: {self.battery_cap} | Speed: {self.speed}"
        
tesla = EV("Tesla", 120, 80)
tesla.going()
tesla.ghost()
print(tesla)

#ElectricTruck that inherits from ElectricVehicle, adds payload_tons, adds a method load() that prints how much it's carrying

class ET(EV):

    def __init__(self, brand, speed, battery_cap, payload):
        super().__init__(brand, speed, battery_cap)
        self.payload = payload

    def load(self):
        self.going()
        print(f"{self.brand} has {self.battery_cap} kw battery capacity and is carrying {self.payload} tons of load")
    
    def __str__(self):
        return f"Electric Truck: {self.brand} | Battery Capacity: {self.battery_cap} | Payload: {self.payload}"
    
mercedes = ET("Mercedes", 100, 200, 15)
mercedes.going()
mercedes.ghost()
mercedes.load()
print(mercedes)