from ds import *

p = creer_pile_vide()
empiler(p, 12)
empiler(p, 14)
empiler(p, 8)
empiler(p, 7)
empiler(p, 19)
empiler(p, 22)

def sommet(p):
    p1 = depiler(p)
    empiler(p, p1)
    return p1

# accès au premier élément sans modifier la pile
# complexité en temps constant

f = creer_file_vide()
enfiler(f, 22)
enfiler(f, 19)
enfiler(f, 7)
enfiler(f, 8)
enfiler(f, 14)
enfiler(f, 12)

def tete(f):
    f_aux = creer_file_vide()
    b = defiler(f)
    enfiler(f_aux, b)
    while not est_file_vide(f):
        enfiler(f_aux, defiler(f))
    while not est_file_vide(f_aux):
        enfiler(f, defiler(f_aux))
    return b

# accès au premier élément sans modifier la pile
# complexite linéaire


def tamis(p):
    """ Pile -> Pile, Pile """
    p_pair, p_impair = creer_pile_vide(), creer_pile_vide()
    while not est_pile_vide(p):
        e = depiler(p)
        if e%2 != 0:
            empiler(p_impair, e)
        else:
            empiler(p_pair, e)
    return p_pair, p_impair
        
def maximum(p):
    """ Pile -> int """
    # initialisation incorrecte si que des nombres < 0
    # maxi = 0
    # Solution 1 (très bien)
    # maxi = depiler(p)
    # Solution 2 (sans dépilement)
    maxi = -float("inf") # valeur initiale plus petite que tous les entiers
    while not est_pile_vide(p):
        c = depiler(p)
        if c > maxi:
            maxi = c
    return maxi
    
def retourne(p):
    """ Pile -> None """
    f_aux = creer_file_vide()
    while not est_pile_vide(p):
        enfiler(f_aux, depiler(p))
    while not est_file_vide(f_aux):
        empiler(p, defiler(f_aux))
    # pas d'instruction return
    # la fonction est exécutée pour son effet de bord
    # on modifie la pile p en place
    
def retourne_mieux(p):
    p_aux = creer_pile_vide()
    while not est_pile_vide(p):
        empiler(p_aux, depiler(p))
    p = p_aux
# est_ce que c'est mieux ?












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















