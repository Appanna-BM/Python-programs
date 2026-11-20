#positional arg

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)

hello("John","Josh","Arya")

# Keyword arg

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)

hello(first="John",middle="Josh",last="Arya")