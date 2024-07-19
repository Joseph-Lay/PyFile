"""PyFile.py
Author: Joseph Lay
Version: 0.1.0 7/18/2024

This file manager uses tkinter for its gui. So far, it can display
the contents of a folder as buttons, and it can move up and down the directory tree.
The folder labelled "Move Up" does not exist and is only for moving up the directory tree.
However, the file buttons do nothing useful yet.
"""


import os
import tkinter as tk

def main():
    # Make the main window.
    window()
    

def window():
    # Make the root window
    global root
    root = tk.Tk()
    root.title("PyFile")
    root.geometry("400x800")

    # Make a frame for display purposes.
    # Needs implementation still
    frame = tk.Frame(root)
    frame.grid()

    # Make a one-time greeting
    global greeting
    greeting = tk.Label(text="Welcom to PyFile!")
    greeting.grid()
    
    # Ready some icons.
    global fileIco
    global foldIco
    fileIco = tk.PhotoImage(file="doc16x16.gif")
    foldIco = tk.PhotoImage(file="fold16x16.png")

    # Display some buttons representing the files.
    btns()

    root.mainloop()

def Window2():
    # Make the helpWin window
    helpWin = tk.Toplevel(root)
    helpWin.title("PyFile Helper")
    helpWin.geometry("200x200")


    lbl = tk.Label(text="PyFile!")
    lbl.pack()
    


def btns():
    """Create buttons for each file and subfolder in the working directory."""
    global buttons
    files = os.listdir()
    print(files)
    # Check if this function has run before.
    if "buttons" in globals():
        # If it has run, delete all previous widgets.
        for widget in root.winfo_children():
                widget.destroy()
                buttons.clear

    # Create a new list for the buttons
    buttons = list(range(len(files)))

    # Start by making a button to move to the parent folder.
    buttons.insert(0, foldBtn(name="../"))
    # Create a button for all the files and folders
    for index in range(len(files)):
        # Start with the folders so that theey are on top.
        if os.path.isdir(files[index]):
            buttons[index] = foldBtn(name=files[index])

    for index in range(len(files)):
        # Afterwards, make the file buttons.
        if os.path.isfile(files[index]):
            buttons[index] = fileBtn(name=files[index])
                

def clicked():
     """Respond to a click on a file."""
     Window2()


def clickFold(folder):
        """Respond to a click on a folder"""
        os.chdir("./"+folder)
        btns()
        return

class fileBtn(tk.Button):
    """Define a new button for a file."""
    def __init__(self, name):
        global fileIco
        self.name = name
        self = tk.Button(text=name, command=clicked, image=fileIco, compound="top")
        self.grid()

class foldBtn(tk.Button):
    """Define a new button for a folder."""
    def __init__(self, name):
        global foldIco
        # If the folder is the one to move up, label it "Move up"
        if name == "../":
             self.name = "Move up"
        # Otherwise, give it the name of the folder it corresponds to.
        else:
            self.name = name
        # Define the button's atrributes
        self = tk.Button(text=self.name, image=foldIco, compound="top", command=lambda: clickFold(name))
        self.grid()


if __name__ == "__main__":
    main()


