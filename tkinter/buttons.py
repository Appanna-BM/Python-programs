from tkinter import *
count=0
def click():
    global count
    count+=1
    print(count)
    
window=Tk()
photo=PhotoImage(file='tkinter/thumbsup.png')
button=Button(window,
               text="Click Me!", 
               command=click,
               font=("Comic Sans", 30),
               fg='Green',
               bg='black',
               activeforeground='Green',
               activebackground='black',
               state=ACTIVE,
               image=photo,
               compound='bottom') # when we use image it automatically overrides the text so we use 'Compound' 
                                  #when we say bottom the image will be in bottom and text at top
button.pack()

window.mainloop()