# Activity 1
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def info(self):
        return f"{self.brand} {self.model} costs ${self.price}"

# Activity 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


if __name__ == "__main__":
    # Activity 1: Smartphone example
    phone = Smartphone("Apple", "iPhone 14", 999)
    print(phone.info())
    phone.call("+263 77 656 8718")

    
    car = Car()
    plane = Plane()

    for vehicle in (car, plane):
        vehicle.move()