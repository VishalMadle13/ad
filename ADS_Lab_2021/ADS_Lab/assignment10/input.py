import sys
import os
import tkinter as tk
from tkinter import *
import tkinter.messagebox

window = tk.Tk()
window.title("Neo4j")
window.geometry("700x500")
blog=tk.StringVar()
blog_title=tk.StringVar()


def submit():
    x=blog_title.get()
    print("The title is : " + x)
    blog.set("")



Label(window,text="NEO4J  ", fg="black",font=("Arial", 25),width=37).grid(row=0,column=0)
Label(window,text="   ", fg="black",font=("Arial", 15),width=37).grid(row=10)
Label(window,text="Input", fg="black",font=("Arial", 15),width=37).grid(row=15)
Label(window,text="   ", fg="black",font=("Arial", 15),width=37).grid(row=20)
name_label = tk.Label(window, text = 'Title', font=('calibre',10, 'bold')).grid(row=70)
name_entry = tk.Entry(window,textvariable = blog_title, font=('calibre',10,'normal')).grid(row=80)
sub_btn=tk.Button(window,text = 'Submit', command = submit).grid(row=110)

window.mainloop()