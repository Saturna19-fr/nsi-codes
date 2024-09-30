from hanoi import hanoi3, autre

def hanoi4(depart, arrivee):
    inter = autre(depart, arrivee)
    hanoi3(depart, inter)
    print(f"{depart} -> {arrivee}")
    hanoi3(inter, arrivee)
    
# hanoi 4 n'est pas une fonction récursive

def hanoi(n, depart, arrivee):
    if n == 1:
        print(f"{depart} -> {arrivee}")
    else:
        inter = autre(depart, arrivee)
        hanoi(n - 1, depart, inter)
        print(f"{depart} -> {arrivee}")
        hanoi(n - 1, inter, arrivee)
        