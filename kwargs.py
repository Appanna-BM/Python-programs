def hello(**kwargs):
    for key,val in kwargs.items():
        print(val, end=" ")

hello(title="Mr.",first="bro",middle="dude",last="code")