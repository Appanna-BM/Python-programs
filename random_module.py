import random

x=random.randint(1,6)
y=random.random()#gives random num between 0 and 1
print(y)
print(x)

l=['rock','paper','scissors']
z=random.choice(l) # generate a random ele from list fo choice
print(z)

#shuffle() method to randomize a collection of choice
cards=[1,2,3,4,5,6,7,8,9,"j","k","q"]
random.shuffle(cards)
print(cards)