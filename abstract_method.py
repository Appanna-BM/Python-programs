from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass 

    @abstractmethod
    def stop():
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("The car stopped")

class MotorCycle(Vehicle):
    def go(self):
        print("You ride the motor cycle")

    def stop(self):
            print("The motorcycle stopped")


car=Car()
motorcycle=MotorCycle()

car.go()
motorcycle.go()
