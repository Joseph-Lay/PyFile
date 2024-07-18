"""PyFile.py
Author: Joseph Lay
Version: 0.0.2 7/14/2024

This file manager uses tkinter for its gui. So far, it can display
the contents of a folder as buttons. However, these do nothing useful yet.
"""


import os
import tkinter as tk
import tkinter.ttk as ttk

def main():
    window()
    #print(os.getcwd())
    #cmd("ls")
    #cmd()
    #print(os.getcwd())
    

def window():
    # Make the root window
    root = tk.Tk()
    root.title("PyFile")
    root.geometry("400x400")

    

    frame = tk.Frame(root)
    frame.grid()

    global greeting
    greeting = tk.Label(text="PyFile!")
    greeting.grid()

    # Make a button with the first file name.

    x = cmd("ls")
    print(x)
    button = list(range(len(x)))
    # Ready some icons.
    global fileIco
    global foldIco
    fileIco = tk.PhotoImage(file="doc16x16.gif")
    foldIco = tk.PhotoImage(file="fold16x16.png")
    # As many files there are, make that many buttons.
    """for index in range(len(x)):
        button.append(tk.Button(frame, text=x[index], command=clicked, image=fileIco, compound="top"))
        if os.path.isdir(x[index]):
            button[index].configure(text=x[index], command=clickFold, image=foldIco)
        button[index].grid()"""
    for index in range(len(x)):
        if os.path.isdir(x[index]):
            button[index] = foldBtn(name=x[index])
        else:
            button[index] = fileBtn(name=x[index])
    root.mainloop()

def clicked():
    return greeting.configure(text="Has Buttons!")


def clickFold():
        
        return greeting.configure(text="Has Folders!")

class fileBtn(tk.Button):
    def __init__(self, name):
        global fileIco
        self.name = name
        self = ttk.Button(text=name, command=clicked, image=fileIco, compound="top")
        self.grid()

class foldBtn(tk.Button):
    def __init__(self, name):
        global foldIco
        self.name = name
        self = ttk.Button(text=name, command=clickFold, image=foldIco, compound="top")
        self.grid()



def cmd(cmd = None):
    """
    Translate user commands
    cmd -- a string. Optional. What command to use."""
    if cmd == None:
        cmd = input("CMD. ")
        args = cmd.split()
        cmd = args[0]
        args = args[1:]
        print(cmd)
    cmd.lower()
    if cmd == "up":
        os.chdir("..")
    
    elif cmd == "ls":
        return os.listdir()
    elif cmd == "cd":
        os.chdir(args[0])
        print(os.listdir)
     

if __name__ == "__main__":
    main()


