import matplotlib.pyplot as plt

# Liste des filières
filieres = ["Génie logiciel", "Réseaux", "Comptabilité", "Marketing"]

# Nombre d'étudiants par filière
effectifs = [48, 25, 30, 37]

# Créer le graphique en barres
plt.bar(filieres, effectifs)

plt.title("Nombre d'étudiants par filière")
plt.xlabel("Filières")
plt.ylabel("Nombre d'étudiants")

plt.show()