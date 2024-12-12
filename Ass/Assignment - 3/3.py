
class Vehicle:
    def speed(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Car(Vehicle):
    def speed(self):
        return "The car is speeding at 120 km/h."

class Bike(Vehicle):
    def speed(self):
        return "The bike is speeding at 80 km/h."

class Train(Vehicle):
    def speed(self):
        return "The train is speeding at 150 km/h."

def show_speed(vehicle):
    print(vehicle.speed())

car = Car()
bike = Bike()
train = Train()

print("Polymorphism Demonstration:")
show_speed(car)   
show_speed(bike)  
show_speed(train)
