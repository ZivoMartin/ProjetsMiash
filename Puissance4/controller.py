from tkinter import messagebox

class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        k = 0
        for i in range(7):
            for j in range(7):
                self.view.boutons[k].config(command=lambda i=j: self.play(i))
                k+=1
        self.view.restart.config(command=self.restart)
        

    def play(self, i):
        result = self.model.play(i)
        self.view.boutons[i+result[0]*7].config(bg=self.model.color)
        if result[1] == -1:
            messagebox.showinfo("Partie finie", self.model.color+" a gagné !")

    def restart(self):
        k = 0
        for i in range(7):
            for j in range(7):
                self.view.boutons[k].config(bg="white")
                k+=1
        self.model.restart()

        
