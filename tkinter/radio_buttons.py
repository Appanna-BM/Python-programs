from tkinter import *

food=["Pizza","Burger","Juice"]

def order():
    if (x.get()==0):
        print("You ordered pizza")
    elif (x.get()==1):
        print("You ordered burger")
    else:
        print("you ordered juice")
window=Tk()

pizzaImage=PhotoImage(file='tkinter/pizza.png')
burgerImage=PhotoImage(file='tkinter/burger.png')
juiceImage=PhotoImage(file='tkinter/juice.png')

foodImages=[pizzaImage, burgerImage, juiceImage]

x=IntVar()

for index in range(len(food)):
    radiobutton=Radiobutton(window, text=food[index], #adds text  to radio buttons
                            variable=x, #groups radio buttons together if they share the same var                            
                            value=index, #assigns each radio button a different value
                            padx=25,
                            pady=25,
                            font=('Impact', 50),
                            image=foodImages[index],
                            compound='left',
                            indicatoron=0, #eliminate circle select indicators
                            width=375,
                            command=order) 
    radiobutton.pack(anchor=W)


window.mainloop()