import matplotlib.pyplot as plt

semaines = ["S1", "S2", "S3", "S4", "S5"]

notes = [12.5, 14, 14, 16, 17]

presence = [85, 100, 85, 80, 100]

# Créer deux sous-graphiques verticaux
fig, axes = plt.subplots(2, 1, sharex=True)

# Premier graphique : les notes
axes[0].plot(semaines, notes, marker="o")
axes[0].set_title("Évolution des notes")
axes[0].set_ylabel("Notes sur 20")

# Deuxième graphique : le taux de présence
axes[1].plot(semaines, presence, marker="o")
axes[1].set_title("Taux de présence")
axes[1].set_xlabel("Semaines")
axes[1].set_ylabel("Présence (%)")

# Ajuster l'espacement
plt.tight_layout()

# Afficher
plt.show()