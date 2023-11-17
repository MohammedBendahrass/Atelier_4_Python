class Etudiant:
    def __init__(self, nom, prenom, cne, age, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.cne = cne
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return f"Etudiant({self.nom}, {self.prenom}, {self.age}, {self.cne}, {self.moyenne})"


Etudiant1 = Etudiant("mohammed", "bendahrass", "X188612", 23, "20")
Etudiant2 = Etudiant("amine", "belaarebi", "X147894", 25, "12")
Etudiant3 = Etudiant("ismail", "zbair", "X123695", 22, "13")

list_Etudiants = [Etudiant1, Etudiant2, Etudiant3]

list_Etudiants_Tries = sorted(
    list_Etudiants, key=lambda etudiant: (etudiant.age, etudiant.moyenne)
)

for etudiant in list_Etudiants_Tries:
    print(etudiant.__dict__)
