class Model:
    def __init__(self, window):
        self.window = window
        self.grille = [None]*7
        for i in range(7):
            self.grille[i] = [" "]*7
        self.color = "yellow"
    
    def play(self, i):
        j = 0
        while(j<=6 and self.grille[i][j] == " "):
            j = j + 1
        self.grille[i][j-1] = self.color
        couleur_actuelle = self.color
        if(self.color=="yellow"):
            self.color="red"
        else:
            self.color="yellow"
        if not self.test_end(i, j-1, couleur_actuelle):
            return [j-1, -1]
        return [j-1, 0]
    
    def test_end(self, i, j, couleur):
        count = 0
        k = j
        while(k<=6 and self.grille[i][k] == couleur):
            count += 1
            k+=1
        k = j-1
        while(k>=0 and self.grille[i][k] == couleur):
            count += 1
            k-=1
        if(count>=4):
            return False
        count = 0
        k = i
        while(k<=6 and self.grille[k][j] == couleur):
            count += 1
            k+=1
        k = i-1
        while(k>=0 and self.grille[k][j] == couleur):
            count += 1
            k-=1
        if(count>=4):
            return False
        count = 0
        k = i
        l = j
        while(k<=6 and l<=6 and self.grille[k][l] == couleur):
            count += 1
            k+=1
            l+=1
        k = i-1
        l = j-1
        while(k>=0 and l>=0 and self.grille[k][j] == couleur):
            count += 1
            k-=1
            l-=1
        if(count>=4):
            return False
        count = 0
        k = i
        l = j
        while(k>=0 and l<=6 and self.grille[k][l] == couleur):
            count += 1
            k-=1
            l+=1
        k = i+1
        l = j-1
        while(k<=6 and l>=0 and self.grille[k][j] == couleur):
            count += 1
            k+=1
            l-=1
        if(count>=4):
            return False
        return True
    
    def restart(self):
        self.grille = [None]*7
        for i in range(7):
            self.grille[i] = [" "]*7
        self.color = "yellow"
