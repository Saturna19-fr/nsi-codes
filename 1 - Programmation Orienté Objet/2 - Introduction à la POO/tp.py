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

class Livre:
    def __init__(self, t, a, n):
        self.titre = t
        self.auteur = a
        self.nb_pages = n

# 3b.
livre1 = Livre('La peste', 'Albert Camus', 59)
livre2 = Livre('Fondation', 'Isaac Asimov', 256)
livre3 = Livre('Liens de sang', 'Octavia Butler', 467)
livre4 = Livre('Les misérables', 'Victor Hugo', 2135)