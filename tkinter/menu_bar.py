from tkinter import *
def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You paste some text")

window = Tk()

saveImage=PhotoImage(file="tkinter/save.png")

menuBar=Menu(window)
window.config(menu=menuBar)

fileMenu=Menu(menuBar, tearoff=0, font=('Arial', 15)) #tearoff to eliminate an annoying line under text 
menuBar.add_cascade(label="File", menu=fileMenu) #gives a dropdown like effect
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Save", command=quit)

editMenu=Menu(menuBar, tearoff=0, font=('Arial', 15))
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()