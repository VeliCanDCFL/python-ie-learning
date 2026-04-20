class Machine:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"Machine: {self.name} | Speed: {self.speed}"