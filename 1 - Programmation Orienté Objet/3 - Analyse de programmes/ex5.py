class Point:
    def __init__(self, x, y):
        """ Point, int, int -> None """
        self.x = x
        self.y = y
        
    def deplace(self, dx, dy):
        """ Point, int, int -> None """
        # méthode qui mute les données
        # muter = modifier
        self.x = self.x + dx
        self.y = self.y + dy

    def symetrique(self):
        """ Point -> Point """
        # la méthode ne mute pas les données
        # elle construit un nouveau point
        # indépendant du point self
        return Point(-self.x, -self.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
class Segment:
    def __init__ (self, d,f):
        """ Segment, Point, Point -> None"""
        self.debut = d
        self.fin = f
        
    def deplace(self, dx, dy):
        """ Segment, float, float -> """
        # self.debut : c'est un objet de type
        # Point. On peut donc lui appliquer
        # une méthode déplace (celle de la classe
        # Point !)
        self.debut.deplace(dx, dy)
        self.fin.deplace(dx, dy)
    
    def symetrique(self):
        """ Segment -> Segment """
        aprime = self.debut.symetrique()
        bprime = self.fin.symetrique()
        return Segment(aprime, bprime)

a = Point(2, 4)
# attributs : x, et y
# méthodes : __init__ , deplace, symetrique, __str__

b = Point(1, 2) # représente B(1 ; 2)
# print(b)
# b.deplace(3, 5)
# print(b)
# b.symetrique()
# print(b)

s1 = Segment(a, b)
# print(a, b)
# s1.deplace(-1, -2)
# print(a, b)
# attention ! la méthode déplace de la classe
# point MODIFIE le point auquel elle s'applique
# on parle de donnée mutable

print(a, b)
sprime = s1.symetrique()
print(a, b)
# la méthode symétrique de la classe Segment
# fait appel à la méthode symétrique de la classe
# Point : les données ne sont pas modifiées
print(sprime.debut, sprime.fin)