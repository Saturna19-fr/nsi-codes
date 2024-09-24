def u(n):
    """ Calcule le n ième terme de la suite
    arithmétique de raison 5 et de premier terme 2 """
    # cas de base
    if n == 0:
        return 2
    # cas général
    else:
        rep_inter = u(n - 1) # appel récursif
        return rep_inter + 5
    
print(u(3))

# def v(n):
#     """ Calcule le n ième terme de la suite
#     géométrique de raison -2 et de premier terme 8 """
#     # cas de base
#     if :
#     # cas général
#     else:
        
