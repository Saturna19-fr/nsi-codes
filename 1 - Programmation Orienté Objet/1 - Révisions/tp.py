def est_pair(bits):
    """ [int] -> bool
    len(bits) > 0
    Détermine si le nombre dont l'écriture en base 2 est donnée par le tableau bits est pair.  """
    if bits[len(bits)] == 1:
        return False
    return True

def est_plus_grand_kbits(bits):
    """ [int] -> bool
    k = len(bits) > 0
    Détermine si le tableau bits correspond
    au plus  grand entier que l'on  puisse
    écrire sur k bits.  """
    for i in range(len(bits)):
        if bits[i] == 0:
            return False
    return True
    # En dessous correct
#     for bit in bits:
#         if bit != 1:
#             return False
#     return True

# Remarque:
# Si t = ['a', 'b', 'c']
# 'a' a pour indice 0 ou -3
# 'b' a pour indice 1 ou -2
# 'c' a pour indice 2 ou -1
# De manière générale : tab[-1] est le dernier élément
# du tableau.

#    for i in range(len(bits)):
# Une boucle bornée (finie), réalise un
# parcours par indice

#     for bit in bits:
# Une boucle bornée (finie), réalise un
# parcours par élément.

# Remarque. 
#     if bits[len(bits) - 1] == 1:
#        return False
#     return True
# On peut écrire autrement :
# return bits[len(bits) - 1] == 0
# On évite les "ifs" inutiles.

def base2_vers_base10(bits):
    """ [int] -> int
    Détermine le nombre entier dont l'écriture en base 2 est donnée par le tableau bits """
    somme = 0
    for i in range(len(bits)):
        # somme = somme + bits[i]*2**(len(bits) - i - 1)
        if bits[i] == 1:
            somme = somme + 2**(len(bits) - i - 1)
    return somme
        
def appartient(tab, e):
    """ [int], int -> bool
    Détermine si l'élément e est présent
    dans le tableau tab.  """
    for elem in tab: # parcours par valeur
        if elem == e:
            return True
    return False
        
#     for i in range(len(tab)): # parcours par indice
#         if tab[i] == e:
#             return True
#     return False

def appartient2(tab, e):
    """ [int], int -> bool """
    for i in range(len(tab)): # parcours par indice
        if tab[i] == e:
            return i
    return -1        

def appartient3(tab, e):
    """ [int], int -> bool """
    for v in range(len(tab) - 1, -1, -1): # parcours par indice
        if tab[v] == e:
            return v 
    return -1     

# range(a, b, c) renvoie la liste des nombres
# de a (inclu) à b (exclu) par pas de c.

def indices_occurrences(tab, e):
    """ [int], int -> [int]
    Détermine les indices des occurrences de e dans le tableau tab.  """
    liste = []
    for i in range(len(tab)): # parcours par indice
        if tab[i] == e:
            liste.append(i)
    return liste

def nombre_occurrences(tab, e):
    """ [int], int -> int
    renvoie le nombre d'occurrences de l'élément e dans le tableau tab"""
    nombre = 0
    for i in range(len(tab)): # parcours par indice
        if tab[i] == e:
            nombre += 1 # pareil que nombre = nombre + 1
    return nombre
    # return len(indices_occurrences(tab, e))

# indices_occurrences réalise n opérations de
# comparaison (==) pour un tableau de taille  n.
# On dit qu'elle a une complexité en O(n) (lu grand
# O de n) ou bien linéaire.

def occurrences(tab):
    """ [int] -> { int:[int] }
    Associe à chaque valeur de tab la liste des indices des occurrences de cette valeur """
    dico = {}
    for i in range(len(tab)):
        cle = tab[i]
        valeur = indices_occurrences(tab, tab[i])
        dico[cle] = valeur
    return dico

# occurrences a une complexité quadratique (on la note
# O(n^2)


def maximum(tab):
    """ [int], int -> int, int
    len(tab) > 0
    Détermine le maximum des éléments de tab, ainsi que le premier indice pour lequel ce maximum est atteint.  """
    maxi = tab[0]
    indice_maxi = 0
    for i in range(1, len(tab)):
        if maxi < tab[i]:
            maxi = tab[i]
            indice_maxi = i
    return maxi, indice_maxi

def est_trie_croissant(tab):
    """ [int] -> bool
    Détermine si le tab est trié par ordre croissant """
    pass

