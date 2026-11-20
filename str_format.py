animal="cow"
item="moon"

#print("The "+animal+"jumped over the "+item)

print("The {0} jumped over the {1}".format(animal, item)) #positional args and 0 and are index
print("The {} jumped over the {}".format(animal, item))#positional args

#print("The {} jumped over the {}".format(animal="cow", item="moon")) #keyword args

text="The {} jumped over the {}"
print(text.format(animal, item))

name="John"
print("Hello my name is {:10}. Nice to meet you".format(name))
print("Hello my name is {:<10}. Nice to meet you".format(name))#left alignment
print("Hello my name is {:>10}. Nice to meet you".format(name)) #right alignment
print("Hello my name is {:^10}. Nice to meet you".format(name))#centre alignment
print("Hello my name is {car:^10}. Nice to meet you".format(car="Honda")) # to display keyword args

#displaying numbers
number=3.1459
n2=1000
print("The number pi is {:.2f}".format(number)) # display only first two digits
print("The number pi is {:b}".format(n2))#binary form of n2
print("The number pi is {:o}".format(n2))#octal form of n2
print("The number pi is {:X}".format(n2))#hexadecimalform
print("The number pi is {:E}".format(n2))#scientific notation form