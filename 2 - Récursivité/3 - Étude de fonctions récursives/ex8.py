def pow(x, n):
    if n == 0:
        return 1
    else:
        res = pow(x, n - 1)
        return x*res
        # return x*pow(x, n - 1)
        
# le nombre de multiplications effectuées
# est de l'ordre de n : algorithme linéaire.
# on fait une multiplication par appel récursif
# et on fait n appel récursifs avant
# d'atteindre le cas de base.

# Exponentiation rapide
# algorithme récursif : appel récursif ligne 23
def pow_fast(x, n):
    """ int, int -> int
    Détermine x^n à l'aide de l'algorithme d'exponentiation rapide. """
    if n == 0:
        return 1
    else:
        p = pow_fast(x, n//2)
        if n%2 == 0:
            return p*p
        else:
            return p*p*x

pow_fast(3, 19)

# dans le pire des cas, cet algorithme effectue
# le  nombre d'appel récursifs * 2
# multiplications
# Or, ici, le nombre d'appel récursifs n'est
# pas proportionnel à n.
# A chaque étape on DIVISE n pas 2
# (on ne se contente pas d'enlever 1 à n)
# On parle de complexité logarithmique.
