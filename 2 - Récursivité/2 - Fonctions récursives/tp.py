def géométrique(n, a, q):
    """ int, float, float -> float
    Renvoie u_n quand (u_n) est une suite géométrique de premier terme a et de raison q. """
    if n == 0:
        return a
    else:
        r=géométrique(n-1, a, q) # appel récursif
        return r*q
   
print(géométrique(3, 6, 2))
# attention aux flottants en python
# géométrique(3,3, 1.1) renvoie
# 3.993000000000001
# or la calculatrice indique
# 3*1.1**3 = 3.993
# Le test
# assert géométrique(3, 3, 1.1) == 3.993
# il échoue ! (à cause des flottants).
# from math import isclose
# assert isclose(géométrique(3, 3, 1.1), 3.993)
# On utilise isclose pour comparer des flottants!

# RecursionError peut survenir lorsque
# le cas de base n'est jamais atteint. 

def arithmétique(n, a, q):
    """ int, float, float -> float
    Renvoie u_n, quand (u_n) est une suite arthimétique de premier terme a et de raison q. """
    if n == 0:
        return a
    else:
        r=arithmétique(n-1, a, q) # appel récursif
        return r + q

def factorielle(n):
    """ int -> int
    Renvoie le nombre n! """
    if n == 0:
        return 1
    else:
        r = factorielle(n-1)
        return r * n
    
def fibonacci(n):
    """ int -> int
    n >= 1
    Détermine le n-ième nombre de Fibonacci avec F_0 = 0, F_1 = 1.  """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        r1 = fibonacci(n-1)
        r2 = fibonacci(n-2)
        return r1 + r2
    
print(fibonacci(4))

def encadre(k):
    """ int -> int
    Détermine le plus grand entier que l'on puisse écrire sur k bits """
    pass

def nombre_bits(n):
    """ int -> int
    Renvoie le nombre de bits nécessaires pour écrire n en base 2 """
    pass

# finir jusqu'ici pour vendredi 27

def appartient_aux(tab, e, i):
    """ [int], int, int -> bool 
    0 <= i <= len(tab)
    Détermine si l'élément e est présent parmi les i premiers éléments du tableau tab. """
    # if i == 0:
        # return ...............................
    # else:
        # On teste si le i-ème élément du tableau est l'élément recherché.
        # if tab[............] == .............:
        #     return ...........................
        # Sinon on recherche l'élément e parmi les i-1 premiers éléments. 
        # else:
        #     return ...........................

def appartient(tab, e):
    """ [int], int -> bool 
    Détermine si l'élément e est présent dans le tableau tab. """
    # return .....................................

def nombre_occurrences_aux(tab, e, i):
    """ [int], int, int -> int
    Détermine le nombre d'éléments de tab d'indice parmi les i premiers qui sont égaux à e.  """
    pass

def nombre_occurrences_aux(tab, e, i):
    """ [int], int, int -> int
    Détermine le nombre d'éléments de tab d'indice parmi qui sont égaux à e.  """
    pass
