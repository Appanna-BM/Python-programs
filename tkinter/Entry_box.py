from tkinter import *

def submit():
    username = entry.get() #get returns string of entry var
    print("Hello :",username)
    entry.config(state=DISABLED) # disable the entry files after input and submit

def delete():
    entry.delete(0, END) # 0 means all char from index 0 to end

def backspace():
    entry.delete(len(entry.get())-1, END)

window=Tk()
entry=Entry(window,
            font=('Arial', 50),
            fg='green',
            bg="black",
            show="*") # show = "*" =replace our actual text with something else useful for password
#entry.insert(0, 'Enter text here')
entry.pack(side='left')

submit_button=Button(window, text='Submit' ,command=submit)
submit_button.pack(side=RIGHT)

delete_button=Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button=Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()