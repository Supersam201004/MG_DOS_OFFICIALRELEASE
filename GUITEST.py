from tkinter import *
import time
def start():
    text = Label(self, text="StartTest",)
    
    text.place(x=70,y=300)
    text.pack()
    

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        text = Label(self, text="Welcome To MG OS! Press The Button Below To Get Started!",)
    
        text.place(x=70,y=300)
        text.pack()

        startbutton = Button( master, command=start())
        
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
