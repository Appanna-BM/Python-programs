class Prey:
    def flee(self):
        print("this animal flees")

class predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(predator):
    pass

class Fish(Prey, predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

