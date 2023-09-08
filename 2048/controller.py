from random import randint
from tkinter import messagebox

class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.gauche.config(command=self.gauche)
        self.view.droite.config(command=self.droite)
        self.view.haut.config(command=self.haut)
        self.view.bas.config(command=self.bas)
        self.view.window.bind("<Left>", lambda event: self.gaucheC(event))
        self.view.window.bind("<Right>", lambda event: self.droiteC(event))
        self.view.window.bind("<Up>", lambda event: self.hautC(event))
        self.view.window.bind("<Down>", lambda event: self.basC(event))
        self.view.BoutonIa.config(command=self.ia)
        self.view.BoutonRestart.config(command=self.restart)
        self.actualiserGrille()
       
    def ia(self):
        def repeat():
            if self.model.jeu:
                response = self.model.mouvementVirtuel(self.model.grille, 0, 2)
                response[1] = str(response[1])
                mouvement = response[0]
                if(mouvement == 'gauche'):
                    print("gauche:" + response[1])
                    self.model.gauche()
                    self.actualiserGrille()
                    self.view.window.after(10, repeat)
                elif(mouvement == "droite"):
                    print("droite:" + response[1])
                    self.model.droite()
                    self.actualiserGrille()
                    self.view.window.after(10, repeat)
                elif(mouvement == "bas"):
                    print("bas:" + response[1])
                    self.model.bas()
                    self.actualiserGrille()
                    self.view.window.after(10, repeat)
                else:
                    print("haut:" + response[1])
                    self.model.haut()
                    self.actualiserGrille()
                    self.view.window.after(10, repeat)
        repeat()

    def restart(self):
        self.model.restart()
        self.actualiserGrille()
    
    def gauche(self):
        self.model.gauche()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")



    def droite(self):
        self.model.droite()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def haut(self):
        self.model.haut()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def bas(self):
        self.model.bas()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def gaucheC(self, event):
        self.model.gauche()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def droiteC(self, event):
        self.model.droite()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def hautC(self, event):
        self.model.haut()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def basC(self, event):
        self.model.bas()
        self.actualiserGrille()
        if(self.model.jeu == False):
            messagebox.showinfo("Partie finie")

    def actualiserGrille(self):
        for i in range(16):
            self.view.label[i].config(text=self.model.grille[i])
            if(self.model.grille[i] == " "):
                self.view.label[i].config(bg="white")
            elif(self.model.grille[i]==2):
                self.view.label[i].config(bg="#EEE4DA")
            elif(self.model.grille[i]==4):
                self.view.label[i].config(bg="#EDE0C8")
            elif(self.model.grille[i]==8):
                self.view.label[i].config(bg="#F2B179")
            elif(self.model.grille[i]==16):
                self.view.label[i].config(bg="#F59563")
            elif(self.model.grille[i]==32):
                self.view.label[i].config(bg="#F67C5F")
            elif(self.model.grille[i]==64):
                self.view.label[i].config(bg="#F65E3B")
            elif(self.model.grille[i] == 128):
                self.view.label[i].config(bg="#EDCF72")
            elif(self.model.grille[i] == 256):
                self.view.label[i].config(bg="#EDCC61")
            elif(self.model.grille[i] == 512):
                self.view.label[i].config(bg="#EDC850")
            elif(self.model.grille[i] == 1024):
                self.view.label[i].config(bg="#EDC53F")
            else:
                self.view.label[i].config(bg="#EDC22E")
           
       