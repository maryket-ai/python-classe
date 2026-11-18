class Etudiant:

    # Constructeur
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return (self.note_cc * 0.4) + (self.note_examen * 0.6)
    
    # 12 exercice 2
class Etudiant:

    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return (self.note_cc * 0.4) + (self.note_examen * 0.6)

    def afficher(self):
        print(f"Nom : {self.nom} | CC : {self.note_cc} | Examen : {self.note_examen}")
        
#12 exercice 3

class Groupe:

    def __init__(self):
        self.etudiants = []

    # Ajouter un étudiant
    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    # Calculer la moyenne générale
    def moyenne_generale(self):
        somme = 0

        for etudiant in self.etudiants:
            somme += etudiant.moyenne()

        return somme / len(self.etudiants)
    
#12 exercice 4

class Delegue(Etudiant):

    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"Je suis {self.nom}, délégué de la filière {self.filiere}."
    
# 12 exercice 5

# Création des étudiants
etudiant1 = Etudiant("Erve", 14, 16)
etudiant2 = Etudiant("Sarah", 17, 18)
etudiant3 = Etudiant("David", 12, 15)

# Création du groupe
groupe = Groupe()

# Ajout des étudiants
groupe.ajouter(etudiant1)
groupe.ajouter(etudiant2)
groupe.ajouter(etudiant3)

# Afficher les informations des étudiants
for etudiant in groupe.etudiants:
    etudiant.afficher()
    print("Moyenne :", etudiant.moyenne())

# Afficher la moyenne générale
print("\nMoyenne générale du groupe :", groupe.moyenne_generale())

# Rechercher le meilleur étudiant
meilleur = groupe.etudiants[0]

for etudiant in groupe.etudiants:
    if etudiant.moyenne() > meilleur.moyenne():
        meilleur = etudiant

# Afficher le meilleur étudiant
print("\nMeilleur étudiant :", meilleur.nom)
print("Sa moyenne :", meilleur.moyenne())