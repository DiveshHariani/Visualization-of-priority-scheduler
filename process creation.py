from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from priorityScheduler import *

class HomePage:
    def __init__(self,root):
        root.bind('<Return>', self.getData)
        self.frame = Frame(root,height=1024, width=1024,bg='white')
        self.frame.pack()
        self.frame.pack_propagate(0)

        self.header=Label(self.frame, text='Create process', font=('Eras Demi ITC bold',30), bg='white')
        self.header.place(x=280, y=25)

        self.num_label = Label(self.frame, text='Enter number of processes : ', font=('Arial',15), bg='white')
        self.num_label.place(x=80, y=150)

        self.pid_label = Label(self.frame, text='Enter process ids(seperated by \',\') : ', font=('Arial',15), bg='white')
        self.pid_label.place(x=80, y=250)

        self.pri_label = Label(self.frame, text='Enter priorities(seperated by \',\') : ', font=('Arial',15), bg='white')
        self.pri_label.place(x=80, y=350)

        self.bt_label = Label(self.frame, text='Enter burst times(seperated by \',\') : ', font=('Arial',15), bg='white')
        self.bt_label.place(x=80, y=450)

        self.at_label = Label(self.frame, text='Enter arrival times(seperated by \',\') : ', font=('Arial',15), bg='white')
        self.at_label.place(x=80, y=550)


        self.spin = ttk.Spinbox(self.frame, from_=1, to=10)
        self.spin.focus()
        self.spin.place(x=350, y=155)

        self.pid_entry = ttk.Entry(self.frame, width=30, justify=CENTER, font=('Arial',15))
        self.pid_entry.place(x=400, y=252)\

        self.pri_entry = ttk.Entry(self.frame, width=30, justify=CENTER, font=('Arial', 15))
        self.pri_entry.place(x=400, y=352)

        self.bt_entry = ttk.Entry(self.frame, width=30, justify=CENTER, font=('Arial', 15))
        self.bt_entry.place(x=400, y=452)

        self.arrival_entry = ttk.Entry(self.frame, width=30, justify=CENTER, font=('Arial', 15))
        self.arrival_entry.place(x=400, y=552)

        self.submit = Button(self.frame, height=40, width=40, bg='white', command = self.getData, borderwidth=0, highlightthickness=0)
        self.img = PhotoImage(file='E:\\add.png')
        self.submit.config(image=self.img)
        self.submit.place(x=450, y=600)

    def getData(self, event=None):
        num_of_pro = int(self.spin.get(), 10)
        pid = self.pid_entry.get().split(',')
        try:
            pri = [int(x) for x in self.pri_entry.get().split(',')]
            bt = [int(x) for x in self.bt_entry.get().split(',')]
            at = [int(x) for x in self.arrival_entry.get().split(',')]
        except ValueError:
            messagebox.showerror('Invalid','Invalid entry in priority or burst time')
        if num_of_pro == len(pid) and num_of_pro == len(pri) and num_of_pro == len(bt) and num_of_pro == len(at):
            window.destroy()
            run(n=num_of_pro, pid=pid, priority=pri, burst_time=bt, arrival_time=at)
        else:
            messagebox.showwarning('Invalid entry', "Please enter valid data")


if __name__ == '__main__':
    window=Tk()
    window.geometry('1024x1024')
    HomePage(window)
    window.mainloop()