from tkinter import *

def submit():
    input=text.get("1.0",END) #1.0 is first line
    print(input)

window=Tk()

text=Text(window,
          bg='light yellow',
            font=('Ink Free', 18),
            height=8,
            width=20,
            padx=15,
            pady=15)
text.pack()

button=Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()