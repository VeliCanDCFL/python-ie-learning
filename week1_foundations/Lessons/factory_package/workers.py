class Worker:
    total_workers = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Worker.total_workers += 1

    def __str__(self):
        return f"Worker: {self.name} | Dept: {self.department}"