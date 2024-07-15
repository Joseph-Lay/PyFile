#from turtle import Turtle
import os
import tkinter as tk
"""def display_dir():
    #make_grid
    pass

def draw_grid(t, x, y, length):
     t.up()
     t.goto(x,y)
     t.setheading(270)
     t.down()
     for count in range(4):
          t.forward(length)
          t.left(90)"""

def main():
    window()
    #print(os.getcwd())
    #cmd("ls")
    #cmd()
    #print(os.getcwd())
    

def window():
    # Make the root window
    root = tk.Tk()
    root.title("TITLE!")
    root.geometry("400x400")

    

    frame = tk.Frame(root)
    frame.grid()

    global greeting
    greeting = tk.Label(text="Hello Phil!")
    greeting.grid()

    # Make a button with the first file name.

    x = cmd("ls")
    print(x)
    button = []
    # As many files there are, make that many buttons.
    for index in range(len(x)):
        button.append(tk.Button(frame, text=x[index], command=clicked))
        button[index].grid()
    root.mainloop()

def clicked():
    return greeting.configure(text="Clicked")

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


