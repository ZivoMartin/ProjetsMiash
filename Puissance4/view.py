import tkinter as tk
class View:
    def __init__(self, window):
        self.window = window
        self.window.title("Puissance 4")
        self.window.geometry("500x500")
        self.boutons = [None]*49
        self.frame = tk.Frame(window)
        self.frame.pack(side="top")
        k = 0
        for i in range(7):
            for j in range(7):
                self.button = tk.Button(self.frame, width=3, height=3)
                self.boutons[k] = self.button
                self.button.grid(row=i, column=j)
                k+=1
        self.restart = tk.Button(self.window, text="restart")
        self.restart.pack(side="bottom")

    def setController(self, controller):
        self.controller = controller