country=input("Enter your country :")


if country.strip().lower()=="india": # for clean input remove the white space using strip() and convert to lower char
    age = int(input('Enter your age :'))
    if age >= 18:
        print("You are an adult")
    elif age <= 0:
        print("You are not born yet")
    else:
        print("Invalid age")
else:
    print("You are not an Indian citizen")