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
import tkinter.ttk as ttk

def main():
    # Make the main window.
    window()
    

def window():
    # Make the root window
    global root
    root = tk.Tk()
    root.title("PyFile")
    root.maxsize()

    # Make a frame for display purposes.
    # Needs implementation still
    
    global outer_frame
    global cTableContainer
    global fTable
    global sbHorizontalScrollBar
    global sbVerticalScrollBar
    outer_frame = tk.Frame(root)
    outer_frame.grid()

    cTableContainer = tk.Canvas(outer_frame)
    fTable = tk.Frame(cTableContainer)
    sbHorizontalScrollBar = tk.Scrollbar(outer_frame, orient="horizontal")
    sbVerticalScrollBar = ttk.Scrollbar(outer_frame, orient="vertical")
    createScrollableContainer()
    

    # Make a one-time greeting
    """global greeting
    greeting = tk.Label(fTable,text="Welcom to PyFile!")
    greeting.grid()"""
    
    # Ready some icons.
    global fileIco
    global foldIco
    fileIco = tk.PhotoImage(file="doc16x16.gif")
    foldIco = tk.PhotoImage(file="fold16x16.png")

    # Display some buttons representing the files.
    btns()

    
    
    root.mainloop()

def createScrollableContainer():
    global cTableContainer
    global fTable
    global sbHorizontalScrollBar
    global sbVerticalScrollBar
    cTableContainer.configure(
        xscrollcommand=sbHorizontalScrollBar.set,
        yscrollcommand=sbVerticalScrollBar.set,
        highlightthickness=0,
        )
    print(outer_frame.winfo_height())
    sbHorizontalScrollBar.configure(command=cTableContainer.xview)
    sbVerticalScrollBar.configure(command=cTableContainer.yview)

    sbHorizontalScrollBar.pack(fill="x", side="bottom", expand=False)
    sbVerticalScrollBar.pack(fill="y", side="right", expand=False)
    cTableContainer.pack(fill="both", side="left", expand=True)
    cTableContainer.create_window(0, 0, window=fTable, anchor="nw")
    

def updateScrollRegion():
    cTableContainer.update_idletasks()
    cTableContainer.config(scrollregion = (0,0,fTable.winfo_width(),fTable.winfo_height()))
    print(outer_frame.winfo_height())
    print(outer_frame.winfo_width())
     

def btns():
    global buttons
    """Create buttons for each file and subfolder in the working directory."""
    # Check if this function has run before.
    if "buttons" in globals():
        # If it has run, delete all previous widgets.
        for widget in fTable.winfo_children():
                widget.destroy()
                buttons.clear

    files = os.listdir()
    print(files)
    
        

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
    updateScrollRegion()
    

def properties_window(name):
    # Make the helpWin window
    helpWin = tk.Toplevel(root)
    helpWin.title("PyFile Helper")
    helpWin.geometry("200x200")


    lbl = tk.Label(helpWin, text="File name: "+name)
    lbl.grid()


def clicked(name):
     """Respond to a click on a file."""
     properties_window(name)


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
        self = tk.Button(fTable, text=name, command=lambda:clicked(name), image=fileIco, compound="top")
        self.pack()

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
        self = tk.Button(fTable, text=self.name, image=foldIco, compound="top", command=lambda: clickFold(name))
        self.pack()


if __name__ == "__main__":
    main()


