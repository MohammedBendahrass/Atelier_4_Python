class Utilisateur:
    _nom = ""
    _email = ""
    _mot_de_passe = ""
    _genre = ""
    _age = 0

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age

    def afficher(self):
        print(
            f"Utilisateur : {self._nom},\t{self._email},\t{self._mot_de_passe},\t{self._genre},\t{self._age}"
        )


class Module:
    __name = ""
    __volume_horaire = 0
    __semestre = ""
    list_Matiere = []

    def __init__(self, name="", volume_horaire=0, semestre=""):
        self.__name = name
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre

    def afficher(self):
        print(f"Module : {self.__name},\t{self.__volume_horaire},\t{self.__semestre}")


class Professeur(Utilisateur):
    __ppr = 0
    __grade = ""
    module = Module()
    list_Matieres = []
    list_Annee_Academique = []

    def __init__(
        self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""
    ):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def afficher(self):
        super().afficher()
        print(f"Professeur : {self.__ppr},\t{self.__grade}")


class Matiere:
    __Nom = ""
    __pourcentage = 0.0
    module = Module()
    list_Annee_Academique = []

    def __init__(self, Nom="", pourcentage=0.0):
        self.__Nom = Nom
        self.__pourcentage = pourcentage

    def afficher(self):
        print(f"Matiere : {self.__Nom},\t{self.__pourcentage}")


class Annee_Academique:
    __annee = ""
    list_Etudiant = []
    list_Module = []
    list_Professeur = []

    def __init__(self, annee=""):
        self.__annee = annee

    def afficher(self):
        print(f"Annee_Academique : {self.__annee}")


class Etudiant(Utilisateur):
    __code_massar = ""
    list_Annee_Academique = []

    def __init__(
        self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""
    ):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def afficher(self):
        super().afficher()
        print(f"Etudiant : {self.__code_massar}")


class Evaluation:
    __note = 0.0
    matiere = Matiere()
    annee_academique = Annee_Academique()
    etudiant = Etudiant()

    def __init__(self, note=0.0):
        self.__note = note

    def afficher(self):
        print(f"Evaluation : {self.__note}")


# Création d'une année académique
annee_academique = Annee_Academique("2023")

# Création d'une matière
mathematiques = Matiere("Mathématiques", 70)

# Création d'un module
module_maths = Module("Mathématiques", 60, "S1")

# Création d'un professeur
professeur = Professeur(
    "youssef",
    "youssef@gmail.com",
    "123456",
    "Homme",
    35,
    "12345",
    "Maître de conférences",
)
professeur.list_Matieres.append(mathematiques)
professeur.list_Annee_Academique.append(annee_academique)

# Création d'un étudiant
etudiant = Etudiant(
    "mohammed", "mohammedbendahrass@gmail.com", "123654789", "Homme", 20, "98765"
)
etudiant.list_Annee_Academique.append(annee_academique)

# Création d'une évaluation
evaluation = Evaluation(85)
evaluation.matiere = mathematiques
evaluation.annee_academique = annee_academique
evaluation.etudiant = etudiant

# Affichage des informations
print("Informations de l'année académique:")
annee_academique.afficher()

print("\nInformations du professeur:")
professeur.afficher()
for matiere in professeur.list_Matieres:
    matiere.afficher()

print("\nInformations de l'étudiant:")
etudiant.afficher()
for annee in etudiant.list_Annee_Academique:
    annee.afficher()

print("\nInformations de l'évaluation:")
evaluation.afficher()
