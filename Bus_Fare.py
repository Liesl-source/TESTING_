class Vehicle:
    def __init__(self, fare):
        self.fare = fare

    def get_fare(self):
        return self.fare


class Bus(Vehicle):
    def get_total_fare(self):
        maintenance_charge = self.fare * 0.10
        total_fare = self.fare + maintenance_charge
        return total_fare


# Example usage
bus = Bus(1000)
print("Total Bus Fare:", bus.get_total_fare())
