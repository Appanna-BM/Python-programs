from tkinter import *

def submit():
    food=[]
    for index in list_box.curselection():
        food.insert(index, list_box.get(index))
    print("You have ordered :")
    for item in food:
        print(item) 
   

def add():
    #list_box.insert(list_box.size(), entryBox.get()) #insert a new item into list box 
    for index in reversed(list_box.curselection()):
        list_box.delete(index)

    list_box.config(height=list_box.size())

def delete():
    list_box.delete(list_box.curselection())
    list_box.config(height=list_box.size())

window = Tk()

list_box=Listbox(window, 
                 bg="#f7FFde",
                 font=('Constantia', 20),
                 width=12,
                 selectmode=MULTIPLE)
list_box.pack()

list_box.insert(1, "Pizza")
list_box.insert(2, "Pasta")
list_box.insert(3, "garlic bread")
list_box.insert(4, "soup")
list_box.insert(5, "Salad")

list_box.config(height=list_box.size()) #adjust the size of listbox dynamicall

entryBox=Entry(window)
entryBox.pack()

submitButton=Button(window, text='Submit', command=submit)
submitButton.pack()

addButton=Button(window, text='add', command=add)
addButton.pack()

deleteButton=Button(window, text='delete', command=delete)
deleteButton.pack()


window.mainloop()