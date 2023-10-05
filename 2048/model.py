from random import randint

class Model():
    def __init__(self, window):
        self.window = window
        self.grille = [" "]*16
        self.apparition(self.grille)
        self.apparition(self.grille)
        self.jeu = True

    def apparition(self, grille):
        if(" " in grille):
            indice = randint(0, 15)
            while(grille[indice] != " "):
                indice = randint(0, 15)
            if(randint(1, 5) == 5):
                grille[indice] = 4
            else:
                grille[indice] = 2

        
    def fusion(self, i, j, grille):
        if(grille[i] != " "):
            grille[i] = grille[i]*2
            grille[j] = " "
        
    def stop(self):
        if " " in self.grille:
            return False
        if(self.grille[0] == self.grille[1] or self.grille[0] == self.grille[4]):
            return False 
        if(self.grille[3] == self.grille[2] or self.grille[3] == self.grille[7]):
            return False    
        if(self.grille[12] == self.grille[11] or self.grille[12] == self.grille[8]):
            return False    
        if(self.grille[15] == self.grille[14] or self.grille[15] == self.grille[11]):
            return False             
        if(self.grille[1] == self.grille[2] or self.grille[1] == self.grille[0] or self.grille[1] == self.grille[5]):
            return False    
        if(self.grille[3] == self.grille[2] or self.grille[2] == self.grille[1] or self.grille[2] == self.grille[6]):
            return False    
        if(self.grille[14] == self.grille[15] or self.grille[14] == self.grille[13] or self.grille[14] == self.grille[10]):
            return False    
        if(self.grille[13] == self.grille[12] or self.grille[13] == self.grille[14] or self.grille[13] == self.grille[9]):
            return False    
        for i in range(4, 12, 4):
            j = 1
            while(j<=2):
                if(self.grille[i+j] == self.grille[i+j-1] or self.grille[i+j] == self.grille[i+j+1] or self.grille[i+j] == self.grille[i+j-4] or self.grille[i+j] == self.grille[i+j+4]):
                    return False 
                j+=1
            if(self.grille[i] == self.grille[i+1] or self.grille[i] == self.grille[i-4] or self.grille[i] == self.grille[i+4]):
                return False    
            if(self.grille[i+3] == self.grille[i+2] or self.grille[i+3] == self.grille[i+7] or self.grille[i+3] == self.grille[i-1]):
                return False    
            
        return True

    
    

    def mouvement(self, direction):
        if(direction == "gauche"):
            i = 1
            while(i<=3):
                for j in range(i, i+16, 4):
                    if(self.grille[j] == self.grille[j-1]):
                        self.fusion(j-1, j, self.grille)
                    elif(self.grille[j-1] == " "):
                        k = j- 1
                        l = 0
                        value = self.grille[j]
                        while(k-l!=-1 and k-l!=3 and k-l!=7 and k-l!=11 and self.grille[k-l] == " "):
                            self.grille[k-l] = value
                            self.grille[k-l+1] = " "
                            l += 1
                        if(k-l>=0 and k-l+1<= 15 and self.grille[k-l] == self.grille[k-l+1]):
                            self.fusion(k-l, k-l+1, self.grille)
                i += 1
        elif(direction == "droite"):
            for i in range(2, -1, -1):
                for j in range(i, i+13, 4):
                    if(self.grille[j] == self.grille[j+1]):
                        self.fusion(j+1, j, self.grille)
                    elif(self.grille[j+1] == " "):
                        k = j+1
                        l = 0
                        value = self.grille[j]
                        while(k+l!=4 and k+l!=8 and k+l!=12 and k+l!=16 and self.grille[k+l] == " "):
                            self.grille[k+l] = value
                            self.grille[k+l-1] = " "
                            l+=1
                        if(k+l<=15 and k+l-1>=0 and self.grille[k+l] == self.grille[k+l-1]):
                            self.fusion(k+l, k+l-1, self.grille)
        elif(direction=="haut"):
            for i in range(4, 16, 4):
                for j in range(i, i+4, 1):
                    if(self.grille[j] == self.grille[j-4]):
                        self.fusion(j-4, j, self.grille)
                    elif(self.grille[j-4] == " "):
                        k = j-4
                        l = 0
                        value = self.grille[j]                        
                        while(k-l!=-4 and k-l!=-3 and k-l!=-2 and k-l!=-1 and self.grille[k-l] == " "):
                            self.grille[k-l] = value
                            self.grille[k-l+4] = " "
                            l+=4
                        if(k-l<=15 and k-l+4>=0 and self.grille[k-l] == self.grille[k-l+4]):
                            self.fusion(k-l, k-l+4, self.grille)
        elif(direction=="bas"):
            for i in range(8, -4, -4):
                for j in range(i, i+4, 1):
                    if(self.grille[j] == self.grille[j+4]):
                        self.fusion(j+4, j, self.grille)
                    elif(self.grille[j+4] == " "):
                        k = j+4
                        l = 0
                        value = self.grille[j]
                        while(k+l!=16 and k+l!=17 and k+l!=18 and k+l!=19 and self.grille[k+l] == " "):
                            self.grille[k+l] = value
                            self.grille[k+l-4] = " "
                            l+=4
                        if(k+l<=15 and k+l-4>=0 and self.grille[k+l] == self.grille[k+l-4]):
                            self.fusion(k+l, k+l-4, self.grille)
        
    
    def gauche(self):
        self.mouvement("gauche")
        if self.stop():
            self.jeu = False
        else:
            self.apparition(self.grille)

    def droite(self):
        self.mouvement("droite")
        if self.stop():
            self.jeu = False
        else:
            self.apparition(self.grille)

    def haut(self):
        self.mouvement("haut")
        if self.stop():
            self.jeu = False
        else:
            self.apparition(self.grille)

    def bas(self):
        self.mouvement("bas")
        if self.stop():
            self.jeu = False
        else:
            self.apparition(self.grille)
        
    def restart(self):
        self.grille = [" "]*16
        self.apparition(self.grille)
        self.apparition(self.grille)
        self.jeu=True
    

    def same(self, grille1, grille2):
        for i in range(16):
            if(grille1[i] != grille2[i]):
                return False
        return True
    
    def mouvementVirtuel(self, grille, turn, coup_avance):
        grille_virtuelle = [None]*16
        for i in range(16):
            grille_virtuelle[i] = grille[i]
        droite_f = ["droite",0]
        bas_f = ["bas", 0]
        haut_f = ['haut', 0]
        gauche_f = ['gauche', 0]

        i = 1
        while(i<=3):
            for j in range(i, i+16, 4):
                if(grille_virtuelle[j] == grille_virtuelle[j-1] and grille_virtuelle[j] != " "):
                    gauche_f[1] += grille_virtuelle[j-1]*2/(turn+1)
                    self.fusion(j-1, j, grille_virtuelle)
                elif(grille_virtuelle[j-1] == " "):
                    k = j- 1
                    l = 0
                    value = grille_virtuelle[j]
                    while(k-l!=-1 and k-l!=3 and k-l!=7 and k-l!=11 and grille_virtuelle[k-l] == " "):
                        grille_virtuelle[k-l] = value
                        grille_virtuelle[k-l+1] = " "
                        l += 1
                    if(k-l>=0 and k-l+1<= 15 and grille_virtuelle[k-l] == grille_virtuelle[k-l+1]and grille_virtuelle[k-l] != " "):
                        gauche_f[1] += grille_virtuelle[k-l]*2/(turn+1)
                        self.fusion(k-l, k-l+1, grille_virtuelle)
            i += 1
        if(turn < coup_avance and not self.same(grille, grille_virtuelle)):
            next_turn = self.mouvementVirtuel(grille_virtuelle, turn+1, coup_avance)
            # print("gauche next turn: ", next_turn[1], " this turn: ", gauche_f[1])
            gauche_f[1] += next_turn[1]
            if(turn == 1):
                gauche_f[1] += 1
        for i in range(16):
            grille_virtuelle[i] = grille[i]

        for i in range(2, -1, -1):
            for j in range(i, i+13, 4):
                if(grille_virtuelle[j] == grille_virtuelle[j+1] and grille_virtuelle[j+1] != " "):
                    droite_f[1] += grille_virtuelle[j]*2/(turn+1)
                    self.fusion(j+1, j, grille_virtuelle)
                elif(grille_virtuelle[j+1] == " "):
                    k = j+1
                    l = 0
                    value = grille_virtuelle[j]
                    while(k+l!=4 and k+l!=8 and k+l!=12 and k+l!=16 and grille_virtuelle[k+l] == " "):
                        grille_virtuelle[k+l] = value
                        grille_virtuelle[k+l-1] = " "
                        l+=1
                    if(k+l<=15 and k+l-1>=0 and grille_virtuelle[k+l] == grille_virtuelle[k+l-1] and grille_virtuelle[k+l] != " "):
                        droite_f[1] += grille_virtuelle[k+l]*2/(turn+1)
                        self.fusion(k+l, k+l-1, grille_virtuelle)
        if(turn < coup_avance and not self.same(grille, grille_virtuelle)):
            next_turn = self.mouvementVirtuel(grille_virtuelle, turn+1, coup_avance)
            # print("droite next turn: ", next_turn[1], " this turn: ", droite_f[1])
            droite_f[1] += next_turn[1]
            if(turn == 1):
                droite_f[1] += 1
        for i in range(16):
            grille_virtuelle[i] = grille[i]

        for i in range(4, 16, 4):
            for j in range(i, i+4, 1):
                if(grille_virtuelle[j] == grille_virtuelle[j-4] and grille_virtuelle[j] != " "):
                    haut_f[1] += grille_virtuelle[j]*2/(turn+1)
                    self.fusion(j-4, j, grille_virtuelle)
                elif(grille_virtuelle[j-4] == " "):
                    k = j-4
                    l = 0
                    value = grille_virtuelle[j]                        
                    while(k-l!=-4 and k-l!=-3 and k-l!=-2 and k-l!=-1 and grille_virtuelle[k-l] == " "):
                        grille_virtuelle[k-l] = value
                        grille_virtuelle[k-l+4] = " "
                        l+=4
                    if(k-l<=15 and k-l-4>=0 and grille_virtuelle[k-l] == grille_virtuelle[k-l-4] and grille_virtuelle[k-l] != " "):
                        haut_f[1] += grille_virtuelle[k-l]*2/(turn+1)
                        self.fusion(k-l, k-l-4, grille_virtuelle)
        if(turn < coup_avance and not self.same(grille, grille_virtuelle)):
            next_turn = self.mouvementVirtuel(grille_virtuelle, turn+1, coup_avance)
            # print("haut next turn: ", next_turn[1], " this turn: ", haut_f[1])
            haut_f[1] += next_turn[1]
            if(turn == 1):
                haut_f[1] += 1
        for i in range(16):
            grille_virtuelle[i] = grille[i]

        for i in range(8, -4, -4):
            for j in range(i, i+4, 1):
                if(grille_virtuelle[j] == grille_virtuelle[j+4] and grille_virtuelle[j] != " "):
                    bas_f[1] += grille_virtuelle[j]*2/(turn+1)
                    self.fusion(j+4, j, grille_virtuelle)

                elif(grille_virtuelle[j+4] == " "):
                    k = j+4
                    l = 0
                    value = grille_virtuelle[j]
                    while(k+l!=16 and k+l!=17 and k+l!=18 and k+l!=19 and grille_virtuelle[k+l] == " "):
                        grille_virtuelle[k+l] = value
                        grille_virtuelle[k+l-4] = " "
                        l+=4
                    if(k+l<=15 and k+l-4>=0 and grille_virtuelle[k+l] == grille_virtuelle[k+l-4] and grille_virtuelle[k+l] != " "):
                        bas_f[1] += grille_virtuelle[k+l]*2/(turn+1)
                        self.fusion(k+l, k+l-4, grille_virtuelle)
        if(turn < coup_avance and not self.same(grille, grille_virtuelle)):
            next_turn = self.mouvementVirtuel(grille_virtuelle, turn+1, coup_avance)
            # print("bas next turn: ", next_turn[1], " this turn: ", bas_f[1])
            bas_f[1] += next_turn[1]
            if(turn == 0):
                bas_f[1] += 1

        gauche = gauche_f[1] 
        droite = droite_f[1] 
        haut = haut_f[1]
        bas = bas_f[1]

        if(bas > haut and bas > droite and bas > gauche and (bas_f[1] != 0 or " " in grille)):
            return bas_f
        elif(droite > haut and droite > gauche and droite > bas and droite_f[1] != 0 ):
            return droite_f
        elif(gauche > haut and gauche > droite and gauche > bas and gauche_f[1] != 0):
            return gauche_f
        elif(bas_f[1] != 0 or " " in grille):
            return bas_f
        elif(haut_f[1] != 0 or " " in grille):
            return haut_f
        elif(droite_f[1] != 0 or " " in grille):
            return droite_f
        elif(gauche_f[1] != 0 or " " in grille):
            return gauche_f
        else:
            return haut_f