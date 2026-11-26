class Animal:
    def eat(self):
        print("This nimal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit=Rabbit()
rabbit.eat()