class Heros:
    def __init__(self, nom, cri_victoire, cri_defaite, force, pdv=10):
        self.nom = nom
        self.cri_victoire = cri_victoire
        self.cri_defaite = cri_defaite
        self.force = force
        self.pdv = pdv
        
    def crier_victoire(self):
        print(self.cri_victoire)

    def crier_defaite(self):
        print(self.cri_defaite)
        
    def recoit_blessure(self, val):
        self.pdv -= val
        # On préfère utiliser la méthode
        self.crier_defaite()
       
        # On ne doit pas utiliser l'attribut
        # cri_defaite !
        # print(self.cri_defaite)
    
    def attaquer(self, other):
        if other.force > self.force:
            print("Rien ne se passe...")
        else:
            self.crier_victoire()
            other.recoit_blessure(1) # bonne manière
            # other.pdv -= 1 # mauvaise manière
            # + crier défaite ! (à ne pas oublier)
            self.force = (self.force + 1)// 2         
        
hercule = Heros("Hercule", "HAN", "Ouch", 99)
limace = Heros("La Limace Folle", "GNIII", "Blup", 100)
hercule.attaquer(limace)
limace.attaquer(hercule)
print(hercule.pdv, limace.pdv)

# pdv est un argument optionnel du constructeur de la classe
# ayant pour valeur par défaut 10
# bigboss = Heros("Grand", "X", "x", 1000, pdv = 1000)

# class Heros:
#     def __init__(self,nom,cv,cd,f,pdv=10):
#         self.nom=nom
#         self.cri_victoire=cv
#         self.cri_défaite=cd
#         self.force=f
#         self.point_de_vie=pdv
# 
# hercule=Heros("Hercule","HAN","Ouch",99)
# print(hercule.point_de_vie)
# hercule.pdv
# hercule n'a pas d'attribut pdv, mais un attribut
# point_de_vie




