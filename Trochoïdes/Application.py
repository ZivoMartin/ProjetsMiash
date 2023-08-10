import tkinter as tk
import math
from tkinter import messagebox

class Application:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Trochoïdes")
        self.window.geometry("900x600")
        self.canvas = tk.Canvas(self.window, width=3000, height=1500)
        self.canvas.pack()
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.mode = tk.Menu(self.menu)
        self.create = tk.Menu(self.menu)
        self.couleur = tk.Menu(self.menu)
        self.menu.add_cascade(label="create", menu=self.create)
        self.menu.add_cascade(label="mode de tracé", menu=self.mode)
        self.menu.add_cascade(label="couleur du tracé", menu=self.couleur)


        self.placer_points_fixe = False
        self.placer_points_mobile = False
        self.placer_le_point = False
        self.point_placed_fixe = 0
        self.ligne_type = "line"
        self.couleur_ligne = "red"
        self.cercle_mobile_tab = [None]*20
        for i in range(15):
            self.cercle_mobile_tab[i] = [None]*20
        for i in range(15):
            self.cercle_mobile_tab[i][0] = 2
            self.cercle_mobile_tab[i][4] = 0
            self.cercle_mobile_tab[i][11] = True
            self.cercle_mobile_tab[i][13] = [None]*180
            self.cercle_mobile_tab[i][14] = 0
        self.i = 0

        self.canvas.bind("<Button-1>", self.clic_canvas)
        self.canvas.bind("<Left>", self.decalLeft)
        self.canvas.bind("<Up>", self.decalTop)
        self.canvas.bind("<Right>", self.decalRight)
        self.canvas.bind("<Down>", self.decalBot)

        self.create.add_command(label="Placer le cercle fixe", command=self.placer_cercle_fixe)
        self.create.add_command(label="Placer le cercle mobile", command=self.placer_cercle_mobile)
        self.create.add_command(label="Placer le point mobile", command=self.placer_point_mobile)
        self.create.add_command(label="Tracer", command= lambda: self.epitrochoide(self.i-1))
        self.create.add_command(label="Recommencer", command=lambda: self.canvas.delete('all'))

        self.mode.add_command(label="tracé continue", command = lambda:self.define_type("line"))
        self.mode.add_command(label="pointillé", command=lambda: self.define_type("tiret"))

        self.couleur.add_command(label="rouge", command=lambda: self.define_color("red"))
        self.couleur.add_command(label="bleue", command=lambda: self.define_color("blue"))
        self.couleur.add_command(label="vert", command=lambda: self.define_color("green"))
        self.couleur.add_command(label="violet", command=lambda: self.define_color("purple"))
        self.couleur.add_command(label="rose", command=lambda: self.define_color("pink"))
        self.couleur.add_command(label="marron", command=lambda: self.define_color("brown"))
        self.couleur.add_command(label="cyan", command=lambda: self.define_color("cyan"))

        self.window.mainloop()

    def define_color(self, color):
        self.couleur_ligne = color

    def define_type(self, type):
        self.ligne_type = type

    def placer_cercle_fixe(self):
        #messagebox.showinfo(message="placez un premier point qui définit le centre, puis un deuxième pour le rayon")
        self.placer_points_fixe = True


    def placer_cercle_mobile(self):
            #messagebox.showinfo(message="Placez un point pour definir le cercle mobile")
            self.placer_points_mobile = True

    def placer_point_mobile(self):
        #messagebox.showinfo(message="placez un premier point sur le cercle fixe, puis un deuxième pour le rayon")
        self.placer_le_point = True

    def clic_canvas(self, event):
        if(self.placer_points_fixe):
            self.canvas.focus_set()
            if(self.point_placed_fixe == 0):
                self.centre_fixe = self.canvas.create_rectangle(event.x-2, event.y-2, event.x+2, event.y+2, fill=self.couleur_ligne)
                self.centre_fixeX = event.x
                self.centre_fixeY = event.y
                self.point_placed_fixe += 1
            else:
                self.canvas.delete(self.centre_fixe)
                self.rayon = int(math.sqrt((event.x-self.centre_fixeX)**2 + (event.y-self.centre_fixeY)**2))
                self.cercleFixe = self.canvas.create_oval(self.centre_fixeX-self.rayon, self.centre_fixeY-self.rayon, self.centre_fixeX+self.rayon, self.centre_fixeY+self.rayon)
                self.placer_points_fixe = False
                self.point_placed_fixe = 0

        elif(self.placer_points_mobile):
            print(self.i)
            if(event.x < self.centre_fixeX + self.rayon and event.y < self.centre_fixeY+self.rayon):
                print(self.cercle_mobile_tab[self.i][1])
                self.cercle_mobile_tab[self.i][1] = self.rayon - int(math.sqrt((event.x-self.centre_fixeX)**2 + (event.y-self.centre_fixeY)**2))
                self.tracer_cercle_mobile(event.x, event.y, self.i)
                self.cercle_mobile_tab[self.i][5] = False
            else:
                self.cercle_mobile_tab[self.i][1] = int(math.sqrt((event.x-self.centre_fixeX)**2 + (event.y-self.centre_fixeY)**2)) - self.rayon
                self.tracer_cercle_mobile(event.x, event.y, self.i)
                self.cercle_mobile_tab[self.i][5] = True

        elif(self.placer_le_point):
            self.cercle_mobile_tab[self.i][6] = event.x
            self.cercle_mobile_tab[self.i][7] = event.y
            self.cercle_mobile_tab[self.i][8] = self.canvas.create_rectangle(event.x-2, event.y-2, event.x+2, event.y+2, fill=self.couleur_ligne)
            self.cercle_mobile_tab[self.i][9] = self.canvas.create_line(event.x, event.y, self.cercle_mobile_tab[self.i][2], self.cercle_mobile_tab[self.i][3])
            self.cercle_mobile_tab[self.i][10] = int(math.sqrt((self.cercle_mobile_tab[self.i][2]-event.x)**2 + (self.cercle_mobile_tab[self.i][3]-event.y)**2))
            self.placer_le_point = False
            self.cercle_mobile_tab[self.i][12] = self.couleur_ligne
            self.i += 1

    def epitrochoide(self, i):
        angle_rad = math.radians(self.cercle_mobile_tab[i][0])
        if(self.cercle_mobile_tab[i][5]):
            x = int(self.centre_fixeX + (self.rayon + self.cercle_mobile_tab[i][1])*math.cos(angle_rad))
            y = int(self.centre_fixeY + (self.rayon + self.cercle_mobile_tab[i][1])*math.sin(angle_rad))
        else:
            x = int(self.centre_fixeX + (self.rayon - self.cercle_mobile_tab[i][1])*math.cos(angle_rad))
            y = int(self.centre_fixeY + (self.rayon - self.cercle_mobile_tab[i][1])*math.sin(angle_rad))
        self.tracer_cercle_mobile(x, y, i)
        x = int(self.cercle_mobile_tab[i][10]*math.cos(angle_rad*8) + x) 
        y = int(self.cercle_mobile_tab[i][10]*math.sin(angle_rad*8) + y) 
        self.canvas.delete(self.cercle_mobile_tab[i][8])
        self.cercle_mobile_tab[i][8] = self.canvas.create_rectangle(x-2, y-2, x+2, y+2, fill=self.couleur_ligne)
        self.canvas.delete(self.cercle_mobile_tab[i][9])
        self.cercle_mobile_tab[i][9] = self.canvas.create_line(x, y, self.cercle_mobile_tab[i][2], self.cercle_mobile_tab[i][3])
        self.cercle_mobile_tab[i][0] += 2
        if(not self.cercle_mobile_tab[i][11]):
            if(self.cercle_mobile_tab[i][13][179] != None):
                    self.canvas.delete(self.cercle_mobile_tab[i][13][self.cercle_mobile_tab[i][14]])
            if(self.ligne_type == "line"):
                self.cercle_mobile_tab[i][13][self.cercle_mobile_tab[i][14]] = self.canvas.create_line(x, y, self.cercle_mobile_tab[i][6], self.cercle_mobile_tab[i][7], fill=self.cercle_mobile_tab[i][12])
            else:
                self.cercle_mobile_tab[i][13][self.cercle_mobile_tab[i][14]] = self.canvas.create_line(x, y, self.cercle_mobile_tab[i][6], self.cercle_mobile_tab[i][7], fill=self.cercle_mobile_tab[i][12], dash=(4, 4))
            self.cercle_mobile_tab[i][14] += 1
            if(self.cercle_mobile_tab[i][14] == 180):
                self.cercle_mobile_tab[i][14] = 0
        else:
            self.cercle_mobile_tab[i][11] = False
        self.cercle_mobile_tab[i][6] = x
        self.cercle_mobile_tab[i][7] = y
        self.window.after(30, lambda: self.epitrochoide(i))
       


    

    def tracer_cercle_mobile(self, x, y, i):
        self.cercle_mobile_tab[i][2] = x
        self.cercle_mobile_tab[i][3] = y
        if(self.cercle_mobile_tab[i][4] != 0):
            self.canvas.delete(self.cercle_mobile_tab[i][4])
        else:
            self.placer_points_mobile = False
        self.cercle_mobile_tab[i][4] = self.canvas.create_oval(x-self.cercle_mobile_tab[i][1], y-self.cercle_mobile_tab[i][1], x+self.cercle_mobile_tab[i][1], y+self.cercle_mobile_tab[i][1])

    def center_mobile(x, y):
        pass

    def decalLeft(self, event):
        self.centre_fixeX -=10
        self.canvas.delete(self.cercleFixe)
        self.cercleFixe = self.canvas.create_oval(self.centre_fixeX-self.rayon, self.centre_fixeY-self.rayon, self.centre_fixeX+self.rayon, self.centre_fixeY+self.rayon)

    
    def decalRight(self, event):
        self.centre_fixeX +=10
        self.canvas.delete(self.cercleFixe)
        self.cercleFixe = self.canvas.create_oval(self.centre_fixeX-self.rayon, self.centre_fixeY-self.rayon, self.centre_fixeX+self.rayon, self.centre_fixeY+self.rayon)
    
    def decalTop(self, event):
        self.centre_fixeY -=10
        self.canvas.delete(self.cercleFixe)
        self.cercleFixe = self.canvas.create_oval(self.centre_fixeX-self.rayon, self.centre_fixeY-self.rayon, self.centre_fixeX+self.rayon, self.centre_fixeY+self.rayon)
    
    def decalBot(self, event):
        self.centre_fixeY +=10
        self.canvas.delete(self.cercleFixe)
        self.cercleFixe = self.canvas.create_oval(self.centre_fixeX-self.rayon, self.centre_fixeY-self.rayon, self.centre_fixeX+self.rayon, self.centre_fixeY+self.rayon)

app = Application()

 

