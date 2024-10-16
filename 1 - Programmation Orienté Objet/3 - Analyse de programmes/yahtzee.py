import random 
class De:
    def __init__(self):
        self.valeur = -1 # le dé n'a pas été lancé

    def lancer(self):
        self.valeur = random.randint(1, 6)
        return self.valeur
    
    def __repr__(self):
        return f"<Dé {self.valeur}>"

class Jeu:
    def __init__(self):
        self.des = []
        self.des_de_cote = []

    def prendre_des(self, n):
        self.des = [De() for _ in range(5)]

    def lancer(self):
        for i in range(len(self.des)):
            d = self.des[i]
            res = d.lancer()
            print(f"Dé numéro {i} : résultat {res}")

    def ecarter(self, nums):
        if len(nums) == 0:
            return
        for i in reversed(sorted(nums)):
            self.des_de_cote.append(self.des[i])
            self.des.pop(i)
        print('Dés gardés', self.des)
        print('Dés écartes', self.des_de_cote)

    def compter_score(self):
        total = 0
        for d in self.des_de_cote:
            total += d.valeur 
        return total

    def jouer(self):
        self.prendre_des(5)
        for _ in range(3):
            self.lancer()
            nums = list(map(int, list(input())))
            self.ecarter(nums)
        return self.compter_score()
    
j = Jeu()
score = j.jouer()
print(score)