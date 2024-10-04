class Chien:
    def __init__(self, nom, poids):
        """ Chien, str, float -> None """
        self.nom = nom
        self.poids = poids

    def aboie(self):
        """ Chien -> None  """
        print(f"{self.nom} fait Ouaf !")

    def mange(self, ration):
        if 0 < ration <= self.poids*0.1:
            self.poids += ration
            self.aboie()
            return True
        return False

c1 = Chien("Medor", 12)
res = c1.mange(0.8)

class Chenil:
    def __init__(self, c):
        """ Chenil, [Chien] -> NoneType """
        self.contenu = c

    def nourrir(self, ration):
        """ Chenil, float -> int """
        noms_chiens_nourris = []
        for c in self.contenu:
            a_mangé = c.mange(ration)
            if a_mangé:
                noms_chiens_nourris.append(c.nom)
        return noms_chiens_nourris

c1, c2, c3, c4 = Chien("Médor", 12), Chien("Milou", 10), Chien("Rex", 22), Chien("Beethoven", 18)
maison = Chenil([c1, c2, c3, c4])
chiens_nourris = maison.nourrir(1.5)
print(chiens_nourris)

def u(n):
    """ int -> int """
    if n <= 0:
        return 3
    else:
        return 3*u(n - 1) + 5
