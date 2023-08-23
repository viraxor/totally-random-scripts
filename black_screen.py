import tkinter as tk

class App():
    def __init__(self):
        self.root = tk.Tk()
        
        self.root.attributes("-fullscreen", True)
        self.root["bg"] = "black"
        self.root["cursor"] = "none"
        
        self.root.bind("<Escape>", exit)
        
        self.root.mainloop()
        
if __name__ == "__main__":
    App()