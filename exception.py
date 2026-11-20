try:
    numerator=int(input("Enter numerator :"))
    denominator=int(input("Enter the denominator :"))
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This is always execute")