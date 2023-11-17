class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Vecteur2D: x = {self.x}, y = {self.y}")

    def __add__(self, autre_vecteur):
        N_x = self.x + autre_vecteur.x
        N_y = self.y + autre_vecteur.y
        return Vecteur2D(N_x, N_y)


class Rectangle:
    def __init__(self, largeur, longeur):
        self.largeur = largeur
        self.longeur = longeur
        self.nom = "Rectangle"

    def afficher(self):
        print(f"{self.nom} : largeur = {self.largeur}, longeur = {self.longeur}")

    def Surface(self):
        return self.largeur * self.longeur


class Carre(Rectangle):
    def __init__(self, cote=1):
        super().__init__(largeur=cote, longeur=cote)
        self.nom = "Carre"


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, origin_x=0.0, origin_y=0.0, extremite_x=1.0, extremite_y=1.0):
        self.orig = Point(origin_x, origin_y)
        self.extr = Point(extremite_x, extremite_y)

    def afficher(self):
        print(
            f"Segment: ({self.orig.x}, {self.orig.y}), ({self.extr.x}, {self.extr.y})"
        )


if __name__ == "__main__":
    V1 = Vecteur2D()
    V2 = Vecteur2D(2, 3)
    V1.afficher()
    V2.afficher()
    Somme_Vecteur = V1 + V2
    Somme_Vecteur.afficher()

    R1 = Rectangle(3, 4)
    C1 = Carre(5)
    R1.afficher()
    C1.afficher()
    print(f"La Surface de Rectangle est : {R1.Surface()}")
    print(f"L a Surface de Carre est : {C1.Surface()}")

    Segment_Test = Segment(1, 2, 3, 4)
    Segment_Test.afficher()
