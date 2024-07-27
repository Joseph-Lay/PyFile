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
<<<<<<< Updated upstream
    root.geometry("400x800")
=======
>>>>>>> Stashed changes

    # Make a frame for display purposes.
    # Needs implementation still
    frame = tk.Frame(root)
    frame.grid()

    # Make a one-time greeting
    global greeting
    greeting = tk.Label(text="Welcom to PyFile!")
    greeting.grid()
    
<<<<<<< Updated upstream
    # Ready some icons.
=======
    global outer_frame
    global nav_frame
    global inner_canvas
    global inner_frame
    global h_scrollbar
    global v_scrollbar
    outer_frame = tk.Frame(root, background="red") # A frame outside of all the content.
    outer_frame.grid()
    nav_frame = tk.Frame(outer_frame, background="blue") # A frame for the navigation buttons.
    nav_frame.pack(fill="both", side="top")
    nav_lbl = tk.Label(nav_frame, text="<- Navigation", background="blue", foreground="yellow", )
    nav_lbl.grid(row=0, column=4, columnspan=3)

    inner_canvas = tk.Canvas(outer_frame) # A canvas to make the scrollbar usable.
    inner_frame = tk.Frame(inner_canvas) # The frame with all the files and folders.
    h_scrollbar = tk.Scrollbar(outer_frame, orient="horizontal")
    v_scrollbar = ttk.Scrollbar(outer_frame, orient="vertical")
    createScrollableContainer()
    # Ready some icons. Used with the buttons.
>>>>>>> Stashed changes
    global fileIco
    global foldIco
    fileIco = tk.PhotoImage(file="doc16x16.gif")
    foldIco = tk.PhotoImage(file="fold16x16.png")

<<<<<<< Updated upstream
    # Display some buttons representing the files.
=======
    # Make buttons to move up, back, and forewards.
    nav_btns = ["Up", "Back", "Forward", "Close"]
    for index in range(len(nav_btns)):
        nav_btns[index] = NavBtn(name=nav_btns[index])
    # Create a search box
    search = SearchBox("search", col=4, row=1)
    srch_lbl = tk.Label(nav_frame, text="Search ->", background="blue", foreground="yellow")
    srch_lbl.grid(column=0, columnspan=3, row=1)
    # Display some buttons representing the files and folders.
>>>>>>> Stashed changes
    btns()

    root.mainloop()

<<<<<<< Updated upstream
def Window2():
    # Make the helpWin window
    helpWin = tk.Toplevel(root)
    helpWin.title("PyFile Helper")
    helpWin.geometry("200x200")


    lbl = tk.Label(text="PyFile!")
    lbl.pack()
    


def btns():
=======

def createScrollableContainer():
    """Change several things to make a functional scrollbar."""
    global inner_canvas
    global inner_frame
    global h_scrollbar
    global v_scrollbar
    inner_canvas.configure(
        xscrollcommand=h_scrollbar.set,
        yscrollcommand=v_scrollbar.set,
        highlightthickness=0,
        )
    inner_canvas.bind_all('<MouseWheel>', lambda event: inner_canvas.yview_scroll(-int(event.delta / 60), "units"))
    h_scrollbar.configure(command=inner_canvas.xview)
    v_scrollbar.configure(command=inner_canvas.yview)

    h_scrollbar.pack(fill="x", side="bottom", expand=False)
    v_scrollbar.pack(fill="y", side="right", expand=False)
    inner_canvas.pack(fill="both", side="bottom", expand=True)
    inner_canvas.create_window(0, 0, window=inner_frame, anchor="nw")


def updateScrollRegion():
    """Resize the scrollbar and where you can scroll at."""
    inner_canvas.update_idletasks()
    inner_canvas.config(scrollregion = (0,0,inner_frame.winfo_width(),inner_frame.winfo_height()))
     

def btns(search=""):
    """Remove previous file/folder buttons and add new ones
    
    This starts by checking if it has run before, and, if it has, removing
    all widgets from its previous run. It then adds a new button for all
    folders and files in the current working directory. By default, the 
    folders should come first in alphabetical order, followed by the files.
    """
    global buttons # This will be a list to hold all the new file and folder buttons.
>>>>>>> Stashed changes
    """Create buttons for each file and subfolder in the working directory."""
    global buttons
    files = os.listdir()
    print(files)
    # Check if this function has run before.
    if "buttons" in globals():
        # If it has run, delete all previous widgets.
<<<<<<< Updated upstream
        for widget in root.winfo_children():
                widget.destroy()
                buttons.clear

=======
        for widget in inner_frame.winfo_children():
                widget.destroy()
                buttons.clear

    files = os.listdir() # Get the names of all the folders and files in the current folder.
        
    # Create a grid to place the buttons
    updateScrollRegion()
    grid_width = (inner_canvas.winfo_width() // 50) -1
    print(grid_width, inner_canvas.winfo_width())
>>>>>>> Stashed changes
    # Create a new list for the buttons
    buttons = list(range(len(files)))

    # Start by making a button to move to the parent folder.
    buttons.insert(0, foldBtn(name="../"))
    # Create a button for all the files and folders
<<<<<<< Updated upstream
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
=======
    col = 0
    row = 0
    # If the user has not searched for anything, display everything.
    if search == "":
        for index in range(len(files)):
            # Start with the folders so that they are on top.
            if os.path.isdir(files[index]):
                buttons[index] = foldBtn(name=files[index], col=col, row=row, parent=inner_frame)
                col += 1
                if col > grid_width:
                    col = 0
                    row += 1
    # If the user has searched for something, only show buttons with that text.
    else:
        for index in range(len(files)):
            # Start with the folders so that they are on top.
            if files[index].find(search) != -1:
                if os.path.isdir(files[index]):
                    buttons[index] = foldBtn(name=files[index], col=col, row=row, parent=inner_frame)
                    col += 1
                    if col > grid_width:
                        col = 0
                        row += 1
    for index in range(len(files)):
        # Afterwards, make the file buttons.
        if files[index].find(search) != -1:
            if os.path.isfile(files[index]):
                buttons[index] = fileBtn(name=files[index], col=col, row=row, parent=inner_frame)
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
        self.size_lbl = tk.Label(self.helpWin,text="Size in bytes: "+str(size))
        self.location_lbl = tk.Label(self.helpWin, text="Location")
        self.parent_lbl = tk.Label(self.helpWin,text=parent,wraplength=200)
        self.close_btn = tk.Button(self.helpWin, text="Close", command=self.close)
        self.name_lbl.grid(sticky="nw")
        self.size_lbl.grid(row=3, sticky="nw")
        self.location_lbl.grid(row=4,sticky="nw")
        self.parent_lbl.grid(sticky="nw")

        self.rename_box = tk.Entry(self.helpWin)
        self.rename_box.insert(0, name)
        self.rename_box.bind("<Return>", lambda event: self.rename(name, self.rename_box.get()))
        self.rename_box.grid(row=1, column=0, sticky="nw")
        self.rename_error = tk.Label(self.helpWin)
        self.rename_error.config(text="Error box")
        self.rename_error.grid(row=2, column=0, sticky="nw")
        self.close_btn.grid(row=6, sticky="nw")

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
        """Ensure that there are no illegal filename characters."""
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

    def close(self):
        """Close the window"""
        self.helpWin.destroy()


def clicked(name):
    """Respond to a click on a file."""
    properties = Properties_window(name)
>>>>>>> Stashed changes


def clickFold(folder):
        """Respond to a click on a folder"""
        os.chdir("./"+folder)
        btns()
        return

class fileBtn(tk.Button):
    """Define a new button for a file."""
<<<<<<< Updated upstream
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
=======
    def __init__(self, name, col, row, parent):
        global fileIco
        self.name = name
        self.collumn = col
        self.row = row
        self.parent = parent
        self = tk.Button(parent, text=name[:7], width=50, height=50, command=lambda:clicked(name), image=fileIco, compound="top",relief="groove")
        self.grid(column=col, row=row)

    def __str__(self):
        return self.name + " is a file displayed under " + str(self.parent) + " inside grid position row "+str(self.row) + " collumn " + str(self.collumn)

class foldBtn():
    """Define a new button for a folder."""
    def __init__(self, name, col, row, parent):
        global foldIco
        # Otherwise, give it the name of the folder it corresponds to.
        self.name = name
        self.parent = parent
        self.row = row
        self.collumn = col
        # Define the button's atrributes
        self = tk.Button(parent, text=self.name[:7], width=50, height=50, image=foldIco, compound="top", command=lambda: clickFold(name))
        self.grid(column=col, row=row)
    
    def __str__(self):
        return self.name + " is a folder displayed under " + str(self.parent) + " inside grid position row "+str(self.row) + " collumn " + str(self.collumn)

class NavBtn():
    hist_pos = -1 # Where are we in the history
    history = [] # The history of our moves
    future = [] # The moves that have been undone
    future_pos = -1 # Like hist_pos but for future

    def __init__(self, name):
        global foldIco
        # If the folder is the one to move up, label it "Move up"
        self.name = name # The name of the Navigation Button
        self = tk.Button(nav_frame, text=self.name, compound="top", command=self.clickNav)
        # Configure the uses for the different buttons.
        if name == "Up":
            self.configure(image=upIco)
            self.grid(column=0,row=0)
        elif name == "Back":
            self.configure(image=backIco)
            self.grid(column=1, row=0)
        elif name == "Close":
            self.configure(text="Close")
            self.grid(column=7,row=0, sticky="ne")
>>>>>>> Stashed changes
        else:
            self.name = name
        # Define the button's atrributes
        self = tk.Button(text=self.name, image=foldIco, compound="top", command=lambda: clickFold(name))
        self.grid()

<<<<<<< Updated upstream
=======
    def clickNav(self):
        # Keep track of how far back the user went.
        if self.name == "Up":
            # Update the history list for the Back/Foreward buttons.
            NavBtn.folder_move(os.getcwd())
            os.chdir("../")
            btns()
            return
        elif self.name == "Back":
            self.go_back()
        elif self.name == "Close":
            exit()
        else:
            self.go_forward()
        
    
    def go_back(self):
        """Use the history list to go back."""
        # Check if the user can move back.
        if NavBtn.hist_pos >= 0:
            NavBtn.future.insert(0, os.getcwd())
            os.chdir(NavBtn.history[NavBtn.hist_pos])
            NavBtn.hist_pos -= 1
            NavBtn.future_pos += 1
            # Update the screen
            btns()
    
    def go_forward(self):
        """Use the future list to go forward."""
        # Check if The user has gone back.
        if NavBtn.future_pos > -1:
            NavBtn.hist_pos += 1
            os.chdir(NavBtn.future[NavBtn.future_pos])
            NavBtn.future_pos -= 1
            # Update the screen
            btns()
    
    def folder_move(previous):
        """Notify the history variables that a move has occured."""
        NavBtn.history.append(previous)
        NavBtn.hist_pos +=1
        NavBtn.future_pos = -1




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
    
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()


