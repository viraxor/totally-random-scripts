import tkinter as tk
from tkinter import messagebox
import random

class App():
    def __init__(self):
        self.errors = [(4, "Windows", "Delete system32?"), 
        (3, "Windows", "Formatting drive C:"),
        (4, "Adware Virus Installer", "Install Adware Virus v1.98 FREE?"),
        (1, "Error", "Incorrect credit card number."),
        (4, "No bitches?", "No bitches?"),
        (2, "Warning", "Your computer is on fire."),
        (1, "", ""),
        (1, "Piracy detected", "Please contact the authorities."),
        (2, "Hey", "You have been warned."),
        (1, "Oops", "Something went wrong."), 
        (1, "Mouse error", "Your mouse has stopped working.\nClick OK to continue."),
        (3, "Important information", "You suck.")]
    
        self.root = tk.Tk()
        
        self.root.bind("<Escape>", self.quit_app)
        self.root.after(100, self.error)
        
        self.root.mainloop()
        
    def error(self):
        #1: error
        #2: warning
        #3: info
        #4: question yes no
        
        self.chosen_error = random.choice(self.errors)
        if self.chosen_error[0] == 1:
            messagebox.showerror(self.chosen_error[1], self.chosen_error[2])
        elif self.chosen_error[0] == 2:
            messagebox.showwarning(self.chosen_error[1], self.chosen_error[2])
        elif self.chosen_error[0] == 3:
            messagebox.showinfo(self.chosen_error[1], self.chosen_error[2])
        elif self.chosen_error[0] == 4:
            messagebox.askyesno(self.chosen_error[1], self.chosen_error[2])
            
        self.root.after(100, self.error)
        
    def quit_app(self, e=None):
        self.root.destroy()
        
if __name__ == "__main__":
    App()