class Worker:
    total_workers = 0  #class attribute
    
    def __init__(self, name, department):
        self.name = name
        Worker.total_workers += 1
        self.department = department
        
    def introduce(self):
        print(f"Hi, I am {self.name}, from {self.department}. We have {Worker.total_workers} workers today.")


w1 = Worker("John", "Production")
w2 = Worker("Alex", "Management")
w3 = Worker("Sarah", "HR")

w1.introduce()
w2.introduce()
w3.introduce()