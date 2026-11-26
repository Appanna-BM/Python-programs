class Duck:
    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck=Duck()
chicken=Chicken()
p=person()

p.catch(chicken)