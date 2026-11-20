#printing symbols in a rectangle shape
rows=int(input("How many rows ? "))
columns=int(input("How many cols ? "))
symbol=input("Enter a symbol to use :")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()