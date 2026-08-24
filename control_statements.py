#Used to alter the sequence" of normal execution


#break statement
numbers=[1,3,5,8,9]

for num in numbers:
    if num%2==0:
        print(f"First even number found {num}")
        break
    print(f"checking {num}")

#Continue statement
number=[1,2,3,4,5]

for num in number:
    if num%2==0:
        continue #skip even numbers
    print(f"Odd numbers are {num}")

#Pass
number=[1,2,3,4,5]
for num in range(5):
    if num == 3:
        pass #TODO:Add logic for 3 later
    print(f"{num}")
