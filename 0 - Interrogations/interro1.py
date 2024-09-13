def minimum(tab):
    """ [int] -> int, [int] """
    mini = tab[0]
    indices = [0]
    for i in range(1, len(tab)):
        if tab[i] < mini:
            mini = tab[i]
            indices = [i]
        elif tab[i] == mini:
            indices.append(i)
    return mini, indices
        
# il faut remplacer 
#    for i in range(1, len(tab)):
# par
#    for i in range(len(tab) - 1, 0, -1):
# Ainsi on parcourt les indices du tableau
# par ordre décroissant :
# len(tab) - 1, len(tab) - 2, ..., 3, 2, 1, 0

def gelees(temp):
    """ [int] -> int """
    duree_gel = 0
    plus_grande_duree = 0
    for t in temp:
        if t <= 0:
            duree_gel += 1
            if duree_gel > plus_grand_duree:
                plus_grand_duree = duree_gel
        else:
            duree_gel = 0
    return plus_grande_duree
