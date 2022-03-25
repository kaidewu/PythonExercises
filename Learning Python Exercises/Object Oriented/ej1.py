class Car:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

car1 = Car(240, 50000)
print(f"Max speed: {car1.max_speed} KM/H\nMilage: {car1.milage} KM")