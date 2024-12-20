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
    l = creer_vide()
    l = ajoute(l, n)
    return l

def nombres(n):
    """ int -> Liste
    Renvoie la liste (n, n-1, n-2, ..., 3, 2, 1) """
    if n == 1:
        return singleton(n)
    else:
        l = nombres(n - 1)
        return ajoute(l, n)

# 2.4 : création de listes III

def nombresII_aux(n, i):
    """ int, int -> Liste
    Renvoie la liste de nombres (i, i + 1, ..., n-1, n) """
    if n == i:
        return singleton(n)
    else:
        r = nombresII_aux(n, i + 1)
        return ajoute(r , i)

def nombresII(n):
    """ int -> Liste
    Renvoie la liste de nombres (1, 2, ..., n-1, n) """
    return nombresII_aux(n, 1)

def longueur(l):
    """ Liste -> int
    Renvoie la longueur de la liste l """
    if est_vide(l):
        return 0
    else:
        r = longueur(queue(l))
        return r + 1 

def somme(l):
    """ Liste -> int
    Calcule la somme des éléments de la liste l """
    # if longueur(l)==0:
    #    return 0
    # if longueur(l)==1:
    if est_singleton(l):    
        return tete(l)
    else:
        r = somme(queue(l))
        return r + tete(l)
        # return somme(queue(l))+tete(l)

def appartient(l, e):
    """ Liste, int -> bool
    Détermine si l'élément e fait partie de la liste l """
    if est_vide(l):
        return False
#.    elif appartient(queue(l), e) or tete(l) == e:
    elif tete(l) == e:
        return True
    else:
        r = appartient(queue(l), e)
        return r
#        if r == True:
#            return True
#        else:
#            return False
     
# Rappel. Si c est un entier : 
# if c == 3:
#     return True
# else:
#     return False
# On peut écrire directement :
# return c == 3

def nombre_occurrences(l, e):
    """ Liste, int -> int
    Compte le nombre d'occurrences de e dans l """
    if est_vide(l):
        return 0
    else:
        r = nombre_occurrences(queue(l), e)
        if tete(l) == e:
            return 1 + r
        else:
            return r

def maximum2(a, b):
    """ int, int -> int
    Calcule l'élément maximum parmis a et b
    """
    return a if a > b else b

def maximum(l):
    """ Liste -> int
    Renvoie le plus grand élément de l """
    if est_singleton(l):
        return tete(l)
    else:
        return maximum2(tete(l), maximum(queue(l)))

def supprime(l, e):
    """ Liste, int -> Liste
    Supprime la première occurrence de e la liste l """
    if est_vide(l):
        return l
    elif tete(l) == e:
        return queue(l)
    else:
        return ajoute(supprime(queue(l)), tete(l))
        
def supprime_tout(l, e):
    """ Liste, int -> Liste
    Supprime la première occurrence de e la liste l """
    if est_vide(l):
        return l
    elif tete(l) == e:
        return supprime_tout(queue(l), e)
    else:
        return ajoute(supprime_tout(queue(l), e), tete(l))

def concatene(l1, l2):
    """ Liste, Liste -> Liste
    Concatène les deux listes """
    if est_vide(l1):
        return l2
    else:
        r = concatene(queue(l1), l2)
        return ajoute(r, tete(l1))

def est_2ton(l):
    """ Liste -> bool """
    if est_vide(l) or est_singleton(l):
        return False
    return est_singleton(queue(l))
# fonction en temps constant : quelque soit la taille
# de la liste, on réalise un nombre constant d'opérations

# ou bien avec la fonction longueur(l) :
# def est_2ton(l):
# 	return longueur(l) == 2
# dans ce cas est_2ton est de complexité linéaire
# (nombre d'opération proportionnel à la taille de la liste)

def divise(l):
    """ Liste -> Liste, Liste
    Divise la liste l en deux listes """
    if est_vide(l):
        return creer_vide(), creer_vide()
    elif est_singleton(l):
        return singleton(tete(l)), creer_vide()
    elif est_2ton(l):
        return singleton(tete(l)), singleton(tete(queue(l)))
    else:
        x1 = tete(l)
        x2 = tete(queue(l))
        l1, l2 = divise(queue(queue(l)))
        return ajoute(l1, x1), ajoute(l2, x2)

def liste_sous_ensembles(E):
    """ list -> list
    Renvoie la liste de tous les sous-ensembles de E """
    pass


