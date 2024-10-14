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
    return l is not None and queue(l) is None 

def singleton(n):
    """ int -> Liste
    Renvoie la liste (n) """
    return ajoute(creer_vide(), n)

def nombres(n):
    """ int -> Liste
    Renvoie la liste (n, n-1, n-2, ..., 3, 2, 1) """

    if n == 1:
        return singleton(1)
    else:
        return ajoute(nombres(n - 1), n)

def nombresII_aux(n, i):
    """ int, int -> Liste
    precondition: 1 <= i <= n
    Renvoie la liste de nombres (i, i + 1, ..., n-1, n) """
    if i == n:
        return singleton(n)
    else:
        return ajoute(nombresII_aux(n, i + 1), i)

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
        return 1 + longueur(queue(l))

def somme(l):
    """ Liste -> int
    Calcule la somme des éléments de la liste l """
    
    if est_vide(l):
        return 0
    else:
        return tete(l) + somme(queue(l))


def appartient(l, e):
    """ Liste, int -> bool
    Détermine si l'élément e fait partie de la liste l """
    # Si la liste (la queue donc) est vide, on renvoie False
    # Sinon, on compare l'élément en tête de la liste avec e
    # Si les deux sont égaux, on renvoie True
    # Sinon, on rappelle la fonction avec la queue de la liste
    # Et on répète le processus
    if est_vide(l):
        return False
    else:
        return tete(l) == e or appartient(queue(l), e)

def nombre_occurrences(l, e):
    """ Liste, int -> int
    Compte le nombre d'occurrences de e dans l """
    if est_vide(l):
        return 0
    else:
        return (1 if (tete(l) == e) else 0)+ nombre_occurrences(queue(l), e)
def maximum2(a, b):
    """ int, int -> int
    Calcule l'élément maximum parmis a et b
    """
    return a if a>b else b

def maximum(l):
    """ Liste -> int
    Renvoie le plus grand élément de l """
    if est_singleton(l):
        return tete(l)
    else:
        maxi = maximum(queue(l))
        return maxi if (maxi > tete(l)) else tete(l)

def supprime(l, e):
    """ Liste, int -> Liste
    Supprime la première occurrence de e la liste l """
    if est_vide(l):
        return l
    elif tete(l) == e:
        return queue(l)
    else:
        return ajoute(supprime(queue(l)), tete(l))
        
def supprime(l, e):
    """ Liste, int -> Liste
    Supprime la première occurrence de e la liste l """
    if est_vide(l):
        return l
    elif tete(l) == e:
        return supprime(queue(l), e)
    else:
        return ajoute(supprime(queue(l), e), tete(l))

def concatene(l1, l2):
    """ Liste, Liste -> Liste
    Concatène les deux listes """
    if est_vide(l1):
        return l2
    else:
        return ajoute(concatene(queue(l1), l2), tete(l1))

def divise(l):
    """ Liste -> Liste, Liste
    Divise la liste l en deux listes """
    d = longueur(l)
    if est_vide(l):
        return creer_vide(), creer_vide()
    elif d == 1:
        return l, creer_vide()
    else:
        return divise(queue(l))

def liste_sous_ensembles(E):
    """ list -> list
    Renvoie la liste de tous les sous-ensembles de E """
    pass

