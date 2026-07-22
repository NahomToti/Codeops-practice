from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"

    @abstractmethod
    def wheels(self):
        """Return the number of wheels for this vehicle."""
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def describe(self):
        base = super().describe()
        return f"{base} (capacity: {self.capacity} tons)"

    def wheels(self):
        return 6


if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "Corolla"),
        Truck("Ford", "F-150", 1.5),
        Car("Honda", "Civic"),
        Truck("Volvo", "FH16", 20),
    ]

    for v in vehicles:
        print(f"{v.describe()} — wheels: {v.wheels()}")