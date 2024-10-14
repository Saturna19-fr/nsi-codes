class Maillon:
    """ Un maillon d'une liste chainée. """
    def __init__(self, v, s):
        """ int, Maillon -> None """
        self.valeur = v
        self.suivant = s

class Liste:
    """ Une liste d'éléments. """
    def __init__(self, m):
        """ Maillon -> None """
        self.head = m

maillon4 = Maillon(1, None)
maillon3 = Maillon(42, maillon4)
maillon2 = Maillon(8, maillon3)
maillon1 = Maillon(3, maillon2)

print(maillon2.valeur)
print(maillon2.suivant)
print(maillon2.suivant.valeur)

m = Maillon(1, None)
m = Maillon(42, m)
m = Maillon(8, m)
m = Maillon(3, m)
# encore plus court :
# m = Maillon(3, Maillon(8, Maillon(42, Maillon(1, None))))
    
print(m.valeur)
print(m.suivant)
print(m.suivant.valeur)

# À compléter
m1= None

m2=Maillon(-1,None)

m3=Maillon(-1,None)
m3=Maillon(9,m3)
m3=Maillon(6,m3)
m3=Maillon(5,m3)

m4=Maillon(13,None)
m4=Maillon(9,m4)
m4=Maillon(-5,m4)

# Ou en une seule ligne à chaque fois :
# m1 = None
# m2 = Maillon(-1,None)
# m3 = Maillon(5,Maillon(6,Maillon(9,Maillon(-1,None))))
# m4 = Maillon(-5,Maillon(9,Maillon(13,None)))

# Question 1 : on est allé trop loin dans la liste
# chaînée : None n'a pas d'attribut valeur


def creer_vide():
    """ () -> Maillon
    Renvoie un maillon vide """
    return None

def est_vide(m):
    """ Maillon -> bool
    Renvoie True si et seulement si le maillon m est le maillon vide """
    # if m == None:
    #     return True
    # else:
    #     return False
    return m == None

def tete(m):
    """ Maillon -> int
    m est non vide
    Renvoie l'attribut valeur du maillon m """
    pass

def queue(m):
    """ Maillon -> Maillon
    m est non vide
    Renvoie le maillon suivant dans la chaine de maillon de tête m. """
    pass

def ajoute(m, e):
    """ Maillon, int -> Maillon
    Renvoie le maillon dont l'attribut valeur est e et l'attribut suivant est m """
    pass

# à finir pour mardi 15

def affiche_rec(m):
    """ Maillon -> None
    Affiche les valeurs de la chaîne dont le premier maillon est m. """
    if est_vide(m):
        print("x")
    else:
        print(tete(m), end = " - ")
        affiche_rec(queue(m))

# affiche_rec(m3)

def affiche_i(m):
    """ Maillon -> None
    Affiche les valeurs de la chaîne dont le premier maillon est m """
    maillon_courant = m
    while not est_vide(maillon_courant):
        print(tete(maillon_courant), end=' - ')
        maillon_courant = queue(maillon_courant)
    print("x")

# affiche_i(m3)
affiche = affiche_i

def longueur(m):
    """ Maillon -> int
    Compte le nombre de maillons présents dans la chaîne dont le premier maillon est m """
    # version itérative
    pass

def element(m, i):
    """ Maillon, int -> int
    m est non vide, 0 <= i < longueur(m)
    Renvoie l'élément d'indice i de la chaîne de maillons dont le premier est m """
    pass

def remplace(m, i, e):
    """ Maillon, int, int -> None
    m est non vide, 0 <= i < longueur(m)
    Remplace par e la valeur du i-ème maillon de la chaine commençant par m """
    pass

def ajoute_position(m, e, i):
    """ Maillon, int, int -> None
    Ajoute l'élément e en i-ième position de la chaine dont le premier maillon est m """
    pass

