with open('test.txt', "w") as file: # write to file
    file.write("My name is John \n This is test file")

with open('test.txt', "a") as file: # append to file 
    file.write("\n\a My name is John \n This is test file")

with open('test.txt', "r") as file:
    print(file.read())
