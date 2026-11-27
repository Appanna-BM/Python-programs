from tkinter import *
def display():
    if (x.get()==1):
        print("You agree")
    else:
        print("You dont agree")
window = Tk()
x=IntVar() #If this want to return  string use StrVar(), but it usually return 0 or 1 so IntVar()
photo=PhotoImage(file='tkinter/thumbsup.png')
check_button = Checkbutton(window, 
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left') # onvalue() and offvalue() are value assigned to associated variable when box is checked
check_button.pack()
window.mainloop()