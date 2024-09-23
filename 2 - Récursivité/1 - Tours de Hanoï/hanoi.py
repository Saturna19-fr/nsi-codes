PILIERS = ['A', 'B', 'C'] 

def autre(depart, arrivee):
    """ Pilier, Pilier -> Pilier
    depart et arrivee sont deux piliers distincts
    Renvoie le troisième pilier. """
    for p in PILIERS:
        if p != depart and p != arrivee:
            return p
    return None


def hanoi(n, depart, arrivee):
    if n <= 0:
        return
    inter = autre(depart, arrivee)
    hanoi(n - 1, depart, inter)
    print(f"{depart}  -> {arrivee}")
    hanoi(n - 1, inter, arrivee)

    
hanoi3 = lambda d, a: hanoi(3, d, a)
hanoi4 = lambda d, a: hanoi(4, d, a)

# print('AB')
# print(hanoi3('A', 'B'))
# print('BA')
# print(hanoi3('B', 'A'))
# print('BC')
# print(hanoi3('B', 'C'))
# print('CA')
# print(hanoi3('C', 'A'))

