from abc import ABC, abstractmethod
import json


# Interface Stockage
class Stockage(ABC):

    @abstractmethod
    def sauvegarder(self, cle, valeur):
        pass

    @abstractmethod
    def charger(self, cle):
        pass


# Stockage en mémoire
class StockageMemoire(Stockage):

    def __init__(self):
        self.donnees = {}

    def sauvegarder(self, cle, valeur):
        self.donnees[cle] = valeur

    def charger(self, cle):
        return self.donnees.get(cle)


# Stockage dans un fichier JSON
class StockageFichier(Stockage):

    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier

    def sauvegarder(self, cle, valeur):

        try:
            with open(self.nom_fichier, "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
        except FileNotFoundError:
            donnees = {}

        donnees[cle] = valeur

        with open(self.nom_fichier, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    def charger(self, cle):

        try:
            with open(self.nom_fichier, "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
        except FileNotFoundError:
            return None

        return donnees.get(cle)


# TEST 1 : stockage en mémoire
memoire = StockageMemoire()

memoire.sauvegarder("nom", "Amina")
memoire.sauvegarder("age", 22)

print("Nom :", memoire.charger("nom"))
print("Age :", memoire.charger("age"))


# TEST 2 : stockage dans un fichier
fichier = StockageFichier("donnees.json")

fichier.sauvegarder("nom", "Paul")
fichier.sauvegarder("ville", "Douala")

print("Nom :", fichier.charger("nom"))
print("Ville :", fichier.charger("ville"))