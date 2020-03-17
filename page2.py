from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class MainPage:
    def __init__(self,root,**kwargs):
        self.frame = Frame(root, height=1024, width=1024)
        self.frame.pack()
        self.frame.grid_propagate(0)

        self.information = LabelFrame(self.frame, height=1024, width =1024)
        self.information.grid(row=0,column=0)
        self.information.grid_propagate(0)

        self.no = Label(self.information, text='Number of processes = {}'.format(kwargs['number']), font=('Arial', 15))
        self.no.grid(row=0,column=0)

        self.process_ids = Label(self.information, text='processes Ids = {}'.format(kwargs['process']), font=('Arial', 15))
        self.process_ids.grid(row=1, column=0)

        self.priority = Label(self.information, text='Respective priorities = {}'.format(kwargs['priority']), font=('Arial', 15))
        self.priority.grid(row=2, column=0)

        self.burst_times = Label(self.information, text='Respective burst times = {}'.format(kwargs['bursts']), font=('Arial', 15))
        self.burst_times.grid(row=3, column=0)

window = Tk()
MainPage(window,number=4,process=(1,2,3,4), priority=(1,2,3,4), bursts=(2,2,2,2))
window.mainloop()