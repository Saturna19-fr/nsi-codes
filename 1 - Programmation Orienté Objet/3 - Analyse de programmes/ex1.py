class Voiture:
    def __init__(self, couleur, kilometrage):
        self.couleur = couleur
        self.kilometrage = kilometrage
    
    def __str__(self):
        """ Voiture -> str """
        return f"La voiture {self.couleur} a {self.kilometrage} kilometres"

    # 3a
    def affiche(self):
        print(f"La voiture {self.couleur} a {self.kilometrage} kilometres")
#        print(affiche.v1)
#        print(affiche.v1)


# on donne souvent aux arguments du
# constructeur de la classe le même
# nom que les attributs correspondants des
# variables de classe.

v1 = Voiture("rouge", 20000)
v2 = Voiture("bleue", 30000)

# 3b
v1.affiche()
v2.affiche()

# 3c.
# lorsque la méthode __str__ est implémentée
# dans le corps d'une classe, alors
# print(v1)
# où v1 est une variable d'instance affiche
# la chaine de caractère renvoyée par
# v1.__str__()
# print(v1)
# est équivalent à
# print(v1.__str__())
