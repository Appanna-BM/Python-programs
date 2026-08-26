# Generate a random number

import random
num = random.randint(1,100)
print("Random number :",num)

#using randrange
num2 = random.randrange(1, 1000, 2)
print("Random number 2 :",num2)

#A random float number
num3 = random.uniform(10, 200)
print(num3)

#Randomly selected item from list
seq=['App',12,'America','India']
num5=random.choice(seq)
print("Random number from a list :",num5)

