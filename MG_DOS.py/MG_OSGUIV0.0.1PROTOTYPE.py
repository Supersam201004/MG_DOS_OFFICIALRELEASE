#MG_OSGUIV0.0.1PROTOTYPE
from tkinter import *

#window
window = Tk()
window.title("Python GUI App")
window.configure(width=500, height=300)
window.configure(bg='lightgray')


text = Text(window, text="Just do it", fg='black')
text.place(x=70,y=90)
text.pack()

window.mainloop()
