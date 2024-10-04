def f(n):
    """ int -> int """
    print(f"Appel f({n})")
    if n == 1:
        print(f"f(1) renvoie 1")
        return 1
    else:
        # res = f(n - 1) + f(n - 1)
        res = 2*f(n-1)
        # ces deux lignes sont
        # mathématiques équivalentes
        # mais pas informatiquement
        # équivalentes
        print(f"f({n}) renvoie {res}")
        return res

# f(n) calcule 2**(n-1)
# il y a de l'ordre de 2**(n -1)
# appels récursifs : chaque appel
# réalise lui meme deux appels récursifs
# c'est très mauvais.