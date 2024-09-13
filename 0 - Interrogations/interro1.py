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
        
def gelees(temp):
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
