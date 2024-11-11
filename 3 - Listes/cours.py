class Maillon:
    """ Un maillon d'une liste chainée. """
    def __init__(self, v, s):
        """ int, Maillon -> None """
        self.valeur = v
        self.suivant = s

def creer_vide() -> Maillon: return None
def est_vide(m: Maillon) -> bool: return m is None
def ajoute(m: Maillon, e: int) -> Maillon: return Maillon(e, m)
def tete(m: Maillon) -> int: return m.valeur
def queue(m: Maillon) -> Maillon: return m.suivant

def affiche_i(m):
    """ Maillon -> None
    Affiche les valeurs de la chaîne dont le premier maillon est m """
    maillon_courant = m
    while not maillon_courant is None:
        print(tete(maillon_courant), end=' - ')
        maillon_courant = maillon_courant.suivant
    print("x")
    
affiche = affiche_i

l = creer_vide()
l = ajoute(l, 4)
l = ajoute(l, 3)
l = ajoute(l, 2)
l = ajoute(l, 1)

def singleton(n):
    """ int -> Liste
    Renvoie la liste (n) """
    l = creer_vide()
    l = ajoute(l, n)
    return l

def concatene(l1, l2):
    """ Liste, Liste -> Liste
    Concatène les deux listes """
    if est_vide(l1):
        return l2
    else:
        r = concatene(queue(l1), l2)
        return ajoute(r, tete(l1))

def inverse(l):
    if est_vide(l):
        return creer_vide()
    else:
        return concatene(inverse(queue(l)), singleton(tete(l)))

def inverse_i(m):
    """ Maillon -> Maillon
    inverse la chaine """
    maillon_courant = m
    reponse = None
    while maillon_courant is not None:
        reponse =  Maillon(maillon_courant.valeur, reponse)
        maillon_courant = maillon_courant.suivant
    return reponse
    
def ajoute_fin(l, e):
    """ Liste, int -> Liste """
    if est_vide(l):
        return singleton(e)
    else:
        r = ajoute_fin(queue(l), e)
        return ajoute(r, tete(l))
        
def ajoute_fin2(m, e):
    """ Liste, int -> None """
    maillon_courant = m
    while maillon_courant.suivant is not None:
        maillon_courant = maillon_courant.suivant
    maillon_courant.suivant = Maillon(e, None)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    