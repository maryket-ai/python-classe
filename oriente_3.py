from typing import Protocol


# Définition du Protocol
class Comparable(Protocol):

    def comparer(self, autre) -> int:
        ...


# Fonction qui compare deux objets
def plus_grand(a: Comparable, b: Comparable):
    if a.comparer(b) > 0:
        return a
    else:
        return b


# Classe qui respecte le Protocol
class Nombre:

    def __init__(self, valeur):
        self.valeur = valeur

    def comparer(self, autre) -> int:
        if self.valeur > autre.valeur:
            return 1
        elif self.valeur < autre.valeur:
            return -1
        else:
            return 0


# Création des objets
n1 = Nombre(15)
n2 = Nombre(20)

# Comparaison
resultat = plus_grand(n1, n2)

print("Le plus grand nombre est :", resultat.valeur)