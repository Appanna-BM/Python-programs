from tkinter import *

def submit():
    print("The Temperature is:"+str(scale.get())+" degrees c")

window=Tk()

hotImage=PhotoImage(file='tkinter/hot.png')
hotLabel=Label(image=hotImage)
hotLabel.pack()

scale=Scale(window, from_= 100, to=0,
            length=600,
            orient=VERTICAL, # how scale should be displayed horizontal or vertical
            font=('consoles', 20),
            tickinterval=10, #numeric indicators on scale
            #showvalue=0 ,#hide current value
            resolution=5, #increment of counter
            troughcolor='yellow',
            fg='#FF1C00',
            bg="black"
            
            )

#scale.set(50) #set the moving scroller inside scale to a length
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider
scale.pack()

coldImage=PhotoImage(file='tkinter/cold.png')
coldLabel=Label(image=coldImage)
coldLabel.pack()

button=Button(window, text='submit', command=submit)
button.pack()

window.mainloop()