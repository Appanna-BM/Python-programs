from tkinter import *
from tkinter import filedialog #open and read content of file

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Windows" ,defaultextension='.txt', 
                                    filetypes=[
                                        ("text file",".txt",),
                                        ("HTML",".html"),
                                        ("All files",".*")
                                    ])

    if file is None :
        return 
    fileText=str(text.get(1.0, END))
    #fileText=input("Enter the text :") #using console window
    file.write(fileText)
    file.close()

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()

text=Text()
text.pack()

window.mainloop()