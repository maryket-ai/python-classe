from abc import ABC, abstractmethod


# INTERFACE
class MoyenPaiement(ABC):

    @abstractmethod
    def payer(self, montant):
        pass


# CLASSE ABSTRAITE
class PaiementBase(MoyenPaiement):

    def verifier_montant(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être supérieur à zéro.")

    @abstractmethod
    def traiter_paiement(self, montant):
        pass

    def payer(self, montant):
        self.verifier_montant(montant)
        return self.traiter_paiement(montant)


# PAIEMENT MOBILE MONEY
class MobileMoney(PaiementBase):

    def traiter_paiement(self, montant):
        return f"Paiement Mobile Money de {montant} FCFA effectué."


# PAIEMENT PAR CARTE
class CarteBancaire(PaiementBase):

    def traiter_paiement(self, montant):
        return f"Paiement par carte de {montant} FCFA effectué."


# PAIEMENT A LA LIVRAISON
class CashLivraison(PaiementBase):

    def traiter_paiement(self, montant):
        return f"Paiement de {montant} FCFA à effectuer à la livraison."


# CREATION DES MOYENS DE PAIEMENT
paiement1 = MobileMoney()
paiement2 = CarteBancaire()
paiement3 = CashLivraison()

# TESTS
print(paiement1.payer(15000))
print(paiement2.payer(25000))
print(paiement3.payer(10000))