class Vehicle:

    def __init__(self,max_speed, mileage):
        self.max_speed= max_speed
        self.mileage= mileage
ModelX= Vehicle(240,18)

print("Model Max Speed:",ModelX.max_speed)
print("Model Mileage:",ModelX.mileage)