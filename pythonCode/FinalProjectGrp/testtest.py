from tkinter import *
from tkinter.ttk import *
root = Tk()

def disable_button():
    button_1['state'] = DISABLED
    print("this is how you disable a buuton after a click")
button_1 = Button(root,text = "Disable this button",command=disable_button)
button_1.pack()
root.mainloop()