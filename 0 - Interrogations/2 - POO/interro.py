def qui_pour_lap(classe, seuil):
    """ {str:int} -> [str] """
    liste_ap = []
    for eleve, moyenne in classe.items():
        if moyenne <= seuil:
            liste_ap.append(eleve)
    return liste_ap

class Compte:
    def __init__(self, titulaire, fonds):
        self.titulaire = titulaire
        self.fonds = fonds

    def recevoir(self, montant):
        self.fonds += montant
        print(f"{self.titulaire} dit merci !")

    def impots(self, pourcent):
        prelevement = self.fonds*pourcent/100
        self.fonds = self.fonds - prelevement
        return prelevement

    def envoyer(self, other, montant):
        if self.fonds < montant:
            print("Fonds insuffisants")
        else: 
            self.fonds -= montant
            print(f"{self.titulaire} envoie {montant}")
            other.recevoir(montant)

def le_plus_riche(banque):
    """ [Compte] -> Compte """
    montant_max = banque[0].fonds
    indice_max = 0
    for i in range(len(banque)):
        if banque[i].fonds > montant_max:
            montant_max = banque[i].fonds
            indice_max = i
    return banque[indice_max] 

def le_moins_riche(banque):
    """ [Compte] -> Compte """
    montant_min = banque[0].fonds
    indice_min = 0
    for i in range(len(banque)):
        if banque[i].fonds < montant_min:
            montant_min = banque[i].fonds
            indice_min = i
    return banque[indice_min] 

def evolue(banque, nb_annees):
    for annee in range(nb_annees):
        plus_riche = le_plus_riche(banque)
        moins_riche = le_moins_riche(banque)
        prelevement = plus_riche.impots(5)
        moins_riche.recevoir(prelevement)
