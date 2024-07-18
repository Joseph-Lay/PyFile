import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("100x100")

    btn = tk.Button(text="text")
    btn.pack()
    
    btn2 = fileBtn()

    root.mainloop()

    

class fileBtn(tk.Button):

    def __init__(self):
        self = tk.Button(text="textClass")
        self.pack()
        

if __name__ == "__main__":
    main()
