from hanoi import hanoi3, autre

def hanoi4(depart, arrivee):
    inter = autre(depart, arrivee)
    hanoi3(depart, inter)
    print(f"{depart} -> {arrivee}")
    hanoi3(inter, arrivee)