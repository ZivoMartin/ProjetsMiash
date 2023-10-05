import tkinter as tk

class View():
    def __init__(self, window):
        self.window = window
        self.window.title("2048")
        self.window.geometry("500x500")

        self.bouton_frame = tk.Frame(self.window)
        self.bouton_frame.pack(side="bottom")
        self.gauche = tk.Button(self.bouton_frame, text="gauche")
        self.bas = tk.Button(self.bouton_frame, text="bas")
        self.haut = tk.Button(self.bouton_frame, text="haut")
        self.droite = tk.Button(self.bouton_frame, text="droite")
        # self.haut.pack()
        # self.gauche.pack(side="left")
        # self.droite.pack(side="right")
        # self.bas.pack()

        self.grille_frame = tk.Frame()
        self.grille_frame.pack(side="top")
        self.label = [None]*16
        k = 0

        for i in range(4):
            for j in range(4):
                label = tk.Label(self.grille_frame, width=10, height=5, relief="solid")
                self.label[k] = label
                label.grid(row=i, column=j)
                k+=1

        self.BoutonIa = tk.Button(self.window, text="Call ia")
        self.BoutonIa.pack(side="left")
        self.BoutonRestart = tk.Button(self.window, text="Restart")
        self.BoutonRestart.pack(side="right")
        self.speed_up = tk.Button(self.window, text="speed up")
        self.speed_down = tk.Button(self.window, text="speed down")
        self.speed_up.pack(side="bottom")
        self.speed_down.pack(side="bottom")




    def setController(self, controller):
        self.controller = controller
