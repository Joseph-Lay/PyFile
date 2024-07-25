"""PyFile.py
Author: Joseph Lay
Version: 0.1.2 7/18/2024

This file manager uses tkinter for its gui. So far, it can display
the contents of a folder as buttons, and it can move up and down the directory tree.
The folders labelled "Move Up,"Back," and "Foreward" do not exist and are only for navigating the directory tree.
However, the file buttons do nothing useful yet, although they are planned to open a properties window.
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
    
    global outer_frame
    global nav_frame
    global cTableContainer
    global fTable
    global sbHorizontalScrollBar
    global sbVerticalScrollBar
    outer_frame = tk.Frame(root, background="red")
    outer_frame.grid()
    nav_frame = tk.Frame(outer_frame, background="blue")
    nav_frame.pack(fill="both", side="top")
    nav_lbl = tk.Label(nav_frame, text="<- Navigation", background="blue", foreground="yellow", )
    nav_lbl.grid(row=0, column=4, columnspan=3)

    cTableContainer = tk.Canvas(outer_frame)
    fTable = tk.Frame(cTableContainer)
    sbHorizontalScrollBar = tk.Scrollbar(outer_frame, orient="horizontal")
    sbVerticalScrollBar = ttk.Scrollbar(outer_frame, orient="vertical")
    createScrollableContainer()
    # Ready some icons.
    global fileIco
    global foldIco
    global foreIco
    global backIco
    global upIco
    global searchIco
    fileIco = tk.PhotoImage(file="doc16x16.gif")
    foldIco = tk.PhotoImage(file="fold16x16.png")
    foreIco = tk.PhotoImage(file="Right8x8.png")
    backIco = tk.PhotoImage(file="Left8x8.png")
    upIco = tk.PhotoImage(file="Up8x8.png")
    searchIco = tk.PhotoImage(file="Search8x8.png")

    # Make buttons to move up, back, and forewards.
    nav_btns = ["Up", "Back", "Foreward"]
    for index in range(len(nav_btns)):
        nav_btns[index] = NavBtn(name=nav_btns[index])
    # Create a search box
    search = SearchBox("search", col=4, row=1)
    srch_lbl = tk.Label(nav_frame, text="Search ->", background="blue", foreground="yellow")
    srch_lbl.grid(column=0, columnspan=3, row=1)
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
    cTableContainer.bind_all('<MouseWheel>', lambda event: cTableContainer.yview_scroll(-int(event.delta / 60), "units"))
    sbHorizontalScrollBar.configure(command=cTableContainer.xview)
    sbVerticalScrollBar.configure(command=cTableContainer.yview)

    sbHorizontalScrollBar.pack(fill="x", side="bottom", expand=False)
    sbVerticalScrollBar.pack(fill="y", side="right", expand=False)
    cTableContainer.pack(fill="both", side="bottom", expand=True)
    cTableContainer.create_window(0, 0, window=fTable, anchor="nw")
    

def updateScrollRegion():
    cTableContainer.update_idletasks()
    cTableContainer.config(scrollregion = (0,0,fTable.winfo_width(),fTable.winfo_height()))
     

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
        

    # Create a new list for the buttons
    buttons = list(range(len(files)))

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
    """Find the details about a file and display them."""
    # Make the window
    helpWin = tk.Toplevel(root)
    helpWin.title("PyFile Helper")
    helpWin.geometry("200x200")

    size = os.path.getsize("./"+name)
    parent = os.path.realpath("./")
    print(name)
    print(parent)

    name_lbl = tk.Label(helpWin, text="File name: "+name)
    size_lbl = tk.Label(helpWin,text="Size: "+str(size))
    parent_lbl = tk.Label(helpWin,text="Location:\n"+parent)
    name_lbl.grid()
    size_lbl.grid()
    parent_lbl.grid()


def clicked(name):
     """Respond to a click on a file."""
     properties_window(name)


def clickFold(folder):
    """Respond to a click on a folder"""
    if "history" not in globals():
        history = []
        history.append(os.getcwd())
        print(history)
    os.chdir("./"+folder)
    btns()
    return

def clickNav(name):
    if "history" not in globals():
        history = []
    if name == "Up":
        history.append(os.getcwd())
        print(history)
        os.chdir("../")
        btns()
        return

class fileBtn():
    """Define a new button for a file."""
    def __init__(self, name):
        global fileIco
        self.name = name
        self = tk.Button(fTable, text=name, command=lambda:clicked(name), image=fileIco, compound="top")
        self.pack()

class foldBtn():
    """Define a new button for a folder."""
    def __init__(self, name):
        global foldIco
        # Otherwise, give it the name of the folder it corresponds to.
        self.name = name
        # Define the button's atrributes
        self = tk.Button(fTable, text=self.name, image=foldIco, compound="top", command=lambda: clickFold(name))
        self.pack()

class NavBtn():
    def __init__(self, name):
        global foldIco
        # If the folder is the one to move up, label it "Move up"
        self.name = name
        self = tk.Button(nav_frame, text=self.name, compound="top", command=lambda: clickNav(name))
        if name == "Up":
            self.configure(image=upIco)
            self.grid(column=0,row=0)
        elif name == "Back":
            self.configure(image=backIco)
            self.grid(column=1, row=0)
        else:
            self.configure(image=foreIco)
            self.grid(column=2, row=0)

class SearchBox():
    def __init__(self, name, col, row):
        self.name = name
        self.entry = tk.Entry(nav_frame)
        self.entry.grid(column=col, row=row)
        self.srchBtn(col, row, 15)

    def searched(self):
        return self.entry.get()

    def srchBtn(self, col, row, height):
        self.btn = tk.Button(nav_frame, image=searchIco, height=height, command=self.searched)
        self.btn.grid(column=col+1, row=row)
    

if __name__ == "__main__":
    main()


