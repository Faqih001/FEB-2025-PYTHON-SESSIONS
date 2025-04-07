class Vehicle:
    def move(self):
        pass  # Placeholder method for all vehicles

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Call the move method for each instance
vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move()
