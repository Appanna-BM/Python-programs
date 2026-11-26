from car_oop import Car

car1 = Car('Honda','Creta',2025,'blue')
car2 = Car('Tata','Safari',2026,'black')
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

print("Wheels :",Car.wheels)
car1.drive()
car1.stop()

car2.drive()
car2.stop()

