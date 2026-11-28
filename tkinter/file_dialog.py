from tkinter import *
from tkinter import filedialog #open and read content of file

def openFile():
    filepath=filedialog.askopenfilename(initialdir="C:\\Windows",#set initial dir to which it should point
                                        title="Open File", #set the title of file dialog
                                    filetypes=(("text files","*.txt"),
                                    ("all files","*.*"))
                                    )
    file=open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button=Button(window, text='open', command=openFile)
button.pack()

window.mainloop()