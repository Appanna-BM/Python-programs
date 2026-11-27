from tkinter import *

window=Tk()
window.title("Labels in TK")
window.geometry("500x500")

#including image with label
photo = PhotoImage(file='tkinter/Logo-Black.png')
label=Label(window, 
            text="Hello World", 
            font=('Arial', 20, 'bold'), 
            fg='green', 
            bg='black',
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=photo,
            compound='bottom') #relief for border style and bd for border visibility 
label.pack()
#label.place(x=60, y=20) #will place label at top left side
#label.pack(pady=60)
#label.pack(padx=90) #pack(padx=(5,10) #left and right padding
window.mainloop()