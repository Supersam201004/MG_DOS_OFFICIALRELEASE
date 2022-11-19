from tkinter import *
import time

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        text = Label(self, text="MG ROBOTICS GUI TEST",)
        text.place(x=70,y=300)
        text.pack()
        
print('Starting...')
time.sleep(1)
print('Starting GUI Interface...')
time.sleep(1)
print('Started.')








root = Tk()
app = Window(root)
root.wm_title("MG_OSV0.0.1")
root.geometry("500x400")
root['bg']='green'
root.mainloop()
