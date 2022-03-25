import tkinter as tk
from tkinter import *
window = tk.Tk()
counter = tk.IntVar(0)
count=0
def enter(e):
    window['bg']='yellow'

def Click1():
    global count
    count += 1
    counter.set(count)
    background2()
def Click2():
    global count
    count -=1
    counter.set(count)
    background2()
box1 = tk.Label(
    window,
    textvariable= counter
)
def background1(e):
    background2()
def background2():
    if counter.get() > 0 :
        window['bg']= 'green'
    elif counter.get() < 0:
        window['bg']='red'
    else:
        window['bg']='gray'

btn1= tk.Button(text='+' ,bg="white", fg="black", padx = 30 , pady = 10, command= Click1)
btn2= tk.Button(text='-' ,bg="white", fg="black", padx = 30 , pady = 10, command= Click2)
btn1.pack()
box1.pack()
btn2.pack()

box1.bind('<Enter>',enter)
box1.bind('<Leave>',background1)
window.mainloop()
