"""PyFile.py
Author: Joseph Lay
Version: 0.1.2 7/18/2024

This file manager uses tkinter for its gui. So far, it can display
the contents of a folder as buttons, and it can move up and down the directory tree.

At the top is the navigation bar. The "Up" button changes the current directory to the
parent folder while "Back" and "Foreward" go backwards and forewards in the navigation
history. The entry bar is used to search the current directory.
"""


import os
import tkinter as tk
import tkinter.ttk as ttk

def main():
    
    # Make the main window.
    window()
    

def window():
    """Create a window with the current directory
    """
    # Make the root window
    global root
    root = tk.Tk()
    root.title("PyFile")
    #root.maxsize()

    # Make an outer frame with navigation, then a canvas 
    # with a scrollbar, then an inner frame to hold the files
    # and folders.
    
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
    # Ready some icons. Used with the buttons.
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
    # Display some buttons representing the files and folders.
    btns()

    
    
    root.mainloop()

def createScrollableContainer():
    """Change several things to make a functional scrollbar."""
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
    """Resize the scrollbar."""
    cTableContainer.update_idletasks()
    cTableContainer.config(scrollregion = (0,0,fTable.winfo_width(),fTable.winfo_height()))
     

def btns(search=""):
    """Remove previous file/folder buttons and add new ones
    
    This starts by checking if it has run before, and, if it has, removing
    all widgets from its previous run. It then adds a new button for all
    folders and files in the current working directory. By default, the 
    folders should come first in alphabetical order, followed by the files.
    """
    global buttons
    """Create buttons for each file and subfolder in the working directory."""
    # Check if this function has run before.
    if "buttons" in globals():
        # If it has run, delete all previous widgets.
        for widget in fTable.winfo_children():
                widget.destroy()
                buttons.clear

    files = os.listdir()    
        
    # Create a grid to place the buttons
    updateScrollRegion()
    grid_width = (cTableContainer.winfo_width() // 50) -1
    print(grid_width, cTableContainer.winfo_width())
    # Create a new list for the buttons
    buttons = list(range(len(files)))

    # Create a button for all the files and folders
    col = 0
    row = 0
    if search == "":
        for index in range(len(files)):
            # Start with the folders so that they are on top.
            if os.path.isdir(files[index]):
                buttons[index] = foldBtn(name=files[index], col=col, row=row)
                col += 1
                if col > grid_width:
                    col = 0
                    row += 1
    else:
        for index in range(len(files)):
            # Start with the folders so that they are on top.
            if files[index].find(search) != -1:
                if os.path.isdir(files[index]):
                    buttons[index] = foldBtn(name=files[index], col=col, row=row)
                    col += 1
                    if col > grid_width:
                        col = 0
                        row += 1

    for index in range(len(files)):
        # Afterwards, make the file buttons.
        if files[index].find(search) != -1:
            if os.path.isfile(files[index]):
                buttons[index] = fileBtn(name=files[index], col=col, row=row)
                col += 1
                if col > grid_width:
                    col = 0
                    row += 1
    updateScrollRegion()




class Properties_window():
    """Find the details about a file and display them in a new window."""
    def __init__(self, name):
        # Make the window
        self.helpWin = tk.Toplevel(root)
        self.helpWin.title("PyFile Helper")
        self.helpWin.geometry("200x200")

        size = os.path.getsize("./"+name)
        parent = os.path.realpath("./")
        print(name)
        print(parent)

        self.name_lbl = tk.Label(self.helpWin, text="File name: "+name)
        self.size_lbl = tk.Label(self.helpWin,text="Size: "+str(size))
        self.parent_lbl = tk.Label(self.helpWin,text="Location:\n"+parent)
        self.name_lbl.grid(sticky="nw")
        self.size_lbl.grid(row=3, sticky="nw")
        self.parent_lbl.grid(sticky="nw")

        self.rename_box = tk.Entry(self.helpWin)
        self.rename_box.insert(0, name)
        self.rename_box.bind("<Return>", lambda event: self.rename(name, self.rename_box.get()))
        self.rename_box.grid(row=1, column=0, sticky="nw")
        self.rename_error = tk.Label(self.helpWin)
        self.rename_error.config(text="Error box")
        self.rename_error.grid(row=2, column=0, sticky="nw")

    def rename(self, oldname, newname):
        """Rename a file."""
        # Check for invalid characters
        if self.check_filename(newname) == True:
            try:
                os.rename(oldname, newname)
            except:
                self.rename_error.configure(text="Error renaming file. Please close this window and try a different name.")
            btns()
    
    def check_filename(self, name):
        name = str(name)
        if name == "":
            self.rename_error.configure(text="Error. Must enter name.")
            return False
        elif name.find('\\') != -1:
            self.rename_error.configure(text="Error. Name cannot contain \\")
            return False
        elif name.find('/') != -1:
            self.rename_error.configure(text="Error. Name cannot contain /")
            return False
        elif name.find('"') != -1:
            self.rename_error.configure(text='Error. Name cannot contain "')
            return False
        elif name.find("%") != -1:
            self.rename_error.configure(text="Error. Name cannot contain %")
            return False
        elif name.find("<") != -1:
            self.rename_error.configure(text="Error. Name cannot contain <")
            return False
        elif name.find(">") != -1:
            self.rename_error.configure(text="Error. Name cannot contain >")
            return False
        elif name.find("*") != -1:
            self.rename_error.configure(text="Error. Name cannot contain *")
            return False
        elif name.find("?") != -1:
            self.rename_error.configure(text="Error. Name cannot contain ?")
            return False
        elif name.find("|") != -1:
            self.rename_error.configure(text="Error. Name cannot contain |")
            return False
        elif name.find(":") != -1:
            self.rename_error.configure(text="Error. Name cannot contain :")
            return False
        else:
            return True



def clicked(name):
    """Respond to a click on a file."""
    properties = Properties_window(name)


def clickFold(folder):
    """Respond to a click on a folder"""
    NavBtn.history.append(os.getcwd())
    print(NavBtn.history)
    os.chdir("./"+folder)
    # Update the history list for the Back/Foreward buttons.
    NavBtn.folder_move(os.getcwd())
    btns()
    return


class fileBtn():
    """Define a new button for a file."""
    def __init__(self, name, col, row):
        global fileIco
        self.name = name
        self = tk.Button(fTable, text=name[:7], width=50, height=50, command=lambda:clicked(name), image=fileIco, compound="top",relief="groove")
        self.grid(column=col, row=row)

class foldBtn():
    """Define a new button for a folder."""
    def __init__(self, name, col, row):
        global foldIco
        # Otherwise, give it the name of the folder it corresponds to.
        self.name = name
        # Define the button's atrributes
        self = tk.Button(fTable, text=self.name[:7], width=50, height=50, image=foldIco, compound="top", command=lambda: clickFold(name))
        self.grid(column=col, row=row)

class NavBtn():
    hist_pos = -1
    history = []

    def __init__(self, name):
        global foldIco
        # If the folder is the one to move up, label it "Move up"
        self.name = name
        self = tk.Button(nav_frame, text=self.name, compound="top", command=self.clickNav)
        if name == "Up":
            self.configure(image=upIco)
            self.grid(column=0,row=0)
        elif name == "Back":
            self.configure(image=backIco)
            self.grid(column=1, row=0)
        else:
            self.configure(image=foreIco)
            self.grid(column=2, row=0)

    def clickNav(self):
        # Keep track of how far back the user went.
        if self.name == "Up":
            NavBtn.history.append(os.getcwd())
            NavBtn.hist_pos += 1
            # Update the history list for the Back/Foreward buttons.
            NavBtn.folder_move(os.getcwd())
            os.chdir("../")
            btns()
            return
        elif self.name == "Back":
            self.go_back()
        
    
    def go_back(self):
        """Use the history list to go back."""
        if NavBtn.hist_pos >= 0:
            os.chdir(NavBtn.history[NavBtn.hist_pos])
            NavBtn.hist_pos -= 1
            btns()
    
    def folder_move(previous):
        NavBtn.history.append(previous)
        NavBtn.hist_pos +=1




class SearchBox():
    def __init__(self, name, col, row):
        self.name = name
        self.entry = tk.Entry(nav_frame)
        self.entry.insert(0, "Search")
        self.entry.bind("<Return>", self.searched)
        self.entry.grid(column=col, row=row)
        self.srchBtn(col, row, 15)

    def searched(self, event="Button Click"):
        print(event)
        print("Heller")
        btns(search=self.entry.get())

    def srchBtn(self, col, row, height):
        self.btn = tk.Button(nav_frame, image=searchIco, height=height, command=self.searched)
        self.btn.grid(column=col+1, row=row)
    

if __name__ == "__main__":
    main()


