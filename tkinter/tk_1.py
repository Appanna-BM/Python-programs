from tkinter import *

window=Tk() # instantiate an instance of window
window.geometry("420x420")
window.title("First GUI")

#Setting the icon for window
icon=PhotoImage(file='tkinter/Logo-Black.png')
window.iconphoto(True, icon)

#changing background
window.config(background='#78ADA6')



window.mainloop() # place window on comp screen , listen for events