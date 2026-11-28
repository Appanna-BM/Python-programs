from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is a info message box', message="You are a preson")
    #messagebox.showwarning(title='Warning', message="You have a virus")
    #messagebox.showerror(title='Error', message='Something went wrong')

    #if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing'):
        #print("You did a thing")
    #else:
        #print("You cancelled a thing")
    
    #if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry'):
        #print("You retried a thing")
    #else:
        #print("You cancelled a thing")

    #if messagebox.askyesno(title='ask yes or no', message='Do you like cake'):
        #print("I like cake too")
    #else:
        #print("why do you like cake")

    '''answer = messagebox.askquestion(title='ask question', message='Do you like rasgulla')
    if answer=='yes':
        print("I like rasgulla too")
    else:
        print("Why do you not like rasgulla")'''

    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you like to code ?',icon='error')
    if (answer==True):
        print("You like to code")
    elif (answer==False):
        print("Why are you watching a tutorial on coding")
    else:
        print("You have dodged the question")

    

window = Tk()

button = Button(window, command=click, text='Click Me')
button.pack()

window.mainloop()