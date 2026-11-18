from abc import ABC, abstractmethod

# Classe abstraite
class Animal(ABC):

    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def crier(self):
        pass

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et je fais : {self.crier()}")

# Classe Chien
class Chien(Animal):

    def crier(self):
        return "Wouf ! Wouf !"


# Classe Chat
class Chat(Animal):

    def crier(self):
        return "Miaou ! Miaou !"


# Création des objets
chien = Chien("Rex")
chat = Chat("Minou")

# Présentation
chien.se_presenter()
chat.se_presenter()