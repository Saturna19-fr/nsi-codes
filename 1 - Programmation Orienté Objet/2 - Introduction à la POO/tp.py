# class Livre:
#     pass

# livre1 = Livre()
# livre1.titre = 'La peste'
# livre1.auteur = 'Camus Albert'
# livre1.nb_pages = 59
# 
# livre2 = Livre()
# livre2.titre = 'Fondation'
# livre2.auteur = 'Isaac Asimov'
# livre2.nb_pages = 256
# 
# def creer_livre(t, a, n):
#     """ str, str, int -> Livre """
#     # livre est ici une variable
#     # LOCALE : elle est "invisible"
#     # depuis l'extérieur de la fonction
#     livre = Livre()
#     livre.titre = t
#     livre.auteur = a
#     livre.nb_pages = n
#     return livre
# 
# livre3 = creer_livre('Liens de sang', 'Octavia Butler',467)

# class Livre:
#     def __init__(self, t, a, n):
#         self.titre = t
#         self.auteur = a
#         self.nb_pages = n
# 
# # 3b.
# livre1 = Livre('La peste', 'Albert Camus', 59)
# livre2 = Livre('Fondation', 'Isaac Asimov', 256)
# livre3 = Livre('Liens de sang', 'Octavia Butler', 467)
# livre4 = Livre('Les misérables', 'Victor Hugo', 2135)
# 
# def affiche(lvr):
#     """ Livre -> None
#     Affiche le livre lvr """
#     titre_livre = lvr.titre
#     pages_tot = lvr.nb_pages
#     nom_auteur = lvr.auteur
#     print(f"< Livre '{titre_livre}', auteur {nom_auteur}, nombre de pages {pages_tot} >")
# 
# def prix(lvr):
#     """ Livre -> float
#     Calcule le prix d'un livre """
#     n = lvr.nb_pages
#     if n <= 100:
#         return (10*n)/100
#     elif 101 <= n <= 1000:
#         return (10*100 + (n - 100)*2)/100
#     else:
#         return (10*100 + 900*2 + (n - 1000)*1)/100
# 
# def prix_reduit(lvr, reduc):
#     """ Livre, int -> float
#     Renvoie le prix du livre après réduction """
#     return prix(lvr)*(1 - reduc/100)

class Livre:
    def __init__(self, t, a, n):
        self.titre = t
        self.auteur = a
        self.nb_pages = n
        self.disponible = 1

    def affiche(self):
        """ Livre -> None """
        titre_livre = self.titre
        auteur_livre = self.auteur
        pages_tot = self.nb_pages
        print(f"< Livre '{titre_livre}', auteur {auteur_livre}, nombre de pages {pages_tot} >")

    def prix(self):
        """ Livre -> float
        Calcule le prix d'un livre """
        if self.nb_pages <= 100:
            return self.nb_pages * 0.10
        elif 100 <= self.nb_pages <= 1000:
            return 100*0.10 + (self.nb_pages - 100)*0.01 
        else: 
            return 100*0.10 + 900*0.02 + (self.nb_pages - 1000)*0.01
    
    # attention au degré d'indentation
    # le premier est toujours l'objet
    # auqel s'applique la méthode
    def prix_reduit(self, reduc):
        """ Livre, int -> float
        Renvoie le prix du livre après réduction """
        return self.prix()*(1 - reduc/100)
    
    def recevoir(self, n):
        self.disponible += n
        
    # TP2 : paragraphe 2.3.4
    def vente(self, reduc):
        if self.disponible > 0:
            prix = self.prix_reduit(reduc)
            self.disponible -= 1
            return round(prix, 2)
        else:
            return 0
        

# Initialisation des variables
livre1 = Livre("La peste", "Camus Albert", 59)
livre2 = Livre("Fondation", "Asimoov Isaac", 265)
livre3 = Livre("Liens de sang", "Octavia Butler", 467)
livre4 = Livre("Les misérables", "Victor Hugo", 2135)
livre5 = Livre("Harry Potter à l'école des sorciers", "J. K. Rowling", 132)

# TP2 : paragraphe 3. Gestion d'une librairie.

def recherche(collection, titre):
    """ [Livre], str -> int
    Renvoie le nombre de livres disponibles
    dans la collection ayant le titre recherché """
    for livre in collection:
        if livre.titre == titre:
            return livre.disponible

collection = [livre1, livre2, livre3, livre4]

class Librairie:
    def __init__(self, c):
        """ Librairie, [Livre] -> None """
        # c est une liste de livres
        self.collection = c

libvide = Librairie([])
# livre1.disponible = 8
livre1.recevoir(7)
















