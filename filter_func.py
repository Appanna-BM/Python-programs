friend=[
    ("John", 16),
    ("Gagan", 21),
    ("Jeevan", 22)
]
age=lambda data: data[1]>=18
drinking_buddies=list(filter(age, friend))
for i in drinking_buddies:
    print(i)