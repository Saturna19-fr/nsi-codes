from Liste import creer_vide, est_vide, tete, queue, ajoute, affiche

# question 2 : l'instruction ajoute(l, 2)
# ne modifie pas la liste d'après l'affichage

l1 = creer_vide()

l2 = creer_vide()
l2 = ajoute(l2, -1)

# On ajoute les élémets les uns après les autres
# en partant de la fin
l3 = creer_vide()
l3 = ajoute(l3, -1)
# on aurait pu directement écrire
# l3 = ajoute(l2, 9)
l3 = ajoute(l3, 9)
l3 = ajoute(l3, 6)
l3 = ajoute(l3, 5)

l4 = creer_vide()
l4 = ajoute(l4, 9)
l4 = ajoute(l4, -5)
l4 = ajoute(l4, 9)
l4 = ajoute(l4, 4)
l4 = ajoute(l4, 9)
l4 = ajoute(l4, -5)

def est_singleton(l):
    """ Liste -> bool
    Détermine si la liste est constituée d'un seul élément. """
    # une liste est constituée d'un seul élément
    # si :
    # la liste n'est pas vide
    # la queue est vide
    if est_vide(l):
        return False
    elif est_vide(queue(l)):
        return True
    else:
        return False
    
    # de manière équivalente :
    # return not est_vide(l) and est_vide(queue(l)) 

def singleton(n):
    """ int -> Liste
    Renvoie la liste (n) """
    pass

def nombres(n):
    """ int -> Liste
    Renvoie la liste (n, n-1, n-2, ..., 3, 2, 1) """
    pass

# compléter jusqu'ici pour lundi

def nombresII_aux(n, i):
    """ int, int -> Liste
    Renvoie la liste de nombres (i, i + 1, ..., n-1, n) """
    pass

def nombresII(n):
    """ int, int -> Liste
    Renvoie la liste de nombres (1, 2, ..., n-1, n) """
    pass

def longueur(l):
    """ Liste -> int
    Renvoie la longueur de la liste l """
    pass

def somme(l):
    """ Liste -> int
    Calcule la somme des éléments de la liste l """
    pass

def appartient(l, e):
    """ Liste, int -> bool
    Détermine si l'élément e fait partie de la liste l """
    pass

def nombre_occurrences(l, e):
    """ Liste, int -> int
    Compte le nombre d'occurrences de e dans l """
    pass

def maximum2(a, b):
    """ int, int -> int
    Calcule l'élément maximum parmis a et b
    """
    pass

def maximum(l):
    """ Liste -> int
    Renvoie le plus grand élément de l """
    pass

def supprime(l, e):
    """ Liste, int -> Liste
    Supprime la première occurrence de e la liste l """
    pass

def concatene(l1, l2):
    """ Liste, Liste -> Liste
    Concatène les deux listes """
    pass

def divise(l):
    """ Liste -> Liste, Liste
    Divise la liste l en deux listes """
    pass

def liste_sous_ensembles(E):
    """ list -> list
    Renvoie la liste de tous les sous-ensembles de E """
    pass

