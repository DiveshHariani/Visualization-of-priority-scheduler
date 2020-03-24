from tkinter import *
from graph import *


def draw(seq_list, process_list):
    stack=[]
    for i in seq_list:
        if stack == [] or stack[-1] != i:
            stack.append(i)
    root = Tk()
    frame=Frame(root,height=600, width=600, bg='white')
    frame.pack()
    frame.pack_propagate(0)


    label = Label(frame, text= stack, font=('Eras Demi ITC bold',20), bg='white', pady=20)
    label.pack(side=TOP)

    move = Button(frame, text='Visualize', command=lambda: onClick(process_list, root), font=('Eras Demi ITC bold',20))
    move.place(x=250, y=100)

def onClick(process_list, root):
    root.destroy()
    plot(process_list)
