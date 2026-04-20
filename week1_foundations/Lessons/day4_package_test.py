from factory_package.machines import Machine
from factory_package.workers import Worker

m1 = Machine("CNC Lathe", 1500)
m2 = Machine("Conveyor Belt", 300)

w1 = Worker("Ali", "Production")
w2 = Worker("Sara", "Quality")

print(m1)
print(m2)
print(w1)
print(w2)
print(f"Total workers: {Worker.total_workers}")