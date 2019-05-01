#for GUI
from tkinter import * 
from tkinter.ttk import *
import threading
import sys
import os
import webbrowser
import sys

# window parameters and start up
window = Tk()
window.title("Virtual Stock Exchange")
window.geometry('350x100')

# catching selected values from radio buttons
selected = IntVar()

# radio buttons 
rad1 = Radiobutton(window,text='Block Chain', value=1, variable=selected) 
rad2 = Radiobutton(window,text='Virtual Mouse', value=2, variable=selected) 

# procedure of radio buttons
def virtualMouse():

   # if block chain is selected
   # Open URL in new window, raising the window if possible.
   if selected.get()==1:
         print("Block Chain Activated")
         url = 'http://127.0.0.1:5000/'
         webbrowser.open_new(url)

   # else vitual mouse is selected    
   else:
        print("Face Mode Activated")
        os.system('python3 face-control.py')

# 
btn1 = Button(window, text="Select", command=virtualMouse)
btn2 = Button(window, text="Exit", command=window.destroy)


# placement of all buttons
rad1.grid(column=1, row=5)
rad2.grid(column=2, row=5) 
btn1.grid(column=3, row=5)
btn2.grid(column=4, row=5)

# open window at end
window.mainloop()
