class Etudiant:

    def __init__(self, nom):
        self.nom = nom
        self.__notes = []

    # Ajouter une note
    def ajouter_note(self, note):

        if note < 0 or note > 20:
            raise ValueError("La note doit être comprise entre 0 et 20.")

        self.__notes.append(note)

    # Propriété moyenne en lecture seule
    @property
    def moyenne(self):

        if len(self.__notes) == 0:
            return 0

        return sum(self.__notes) / len(self.__notes)


# Création d'un étudiant
etudiant = Etudiant("Amina")

# Ajout des notes
etudiant.ajouter_note(14)
etudiant.ajouter_note(16)
etudiant.ajouter_note(18)

# Affichage de la moyenne
print("Moyenne de", etudiant.nom, ":", etudiant.moyenne)


# Tentative de modification de la moyenne
try:
    etudiant.moyenne = 15
except AttributeError as erreur:
    print("Erreur :", erreur)