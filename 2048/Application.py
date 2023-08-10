import tkinter as tk
from view import View
from model import Model
from controller import Controller

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        model = Model(self)
        view = View(self)
        controller = Controller(model, view)
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()