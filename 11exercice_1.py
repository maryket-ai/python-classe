import matplotlib.pyplot as plt

notes = [12, 14, 10, 15, 16, 18, 17, 8, 18, 15]

evaluations = [
    "Eval 1", "Eval 2", "Eval 3", "Eval 4", "Eval 5",
    "Eval 6", "Eval 7", "Eval 8", "Eval 9", "Eval 10"
]

# Tracer la courbe
plt.plot(evaluations, notes)

plt.title("Évolution des notes de l'étudiant")

plt.xlabel("Évaluations")
plt.ylabel("Notes sur 20")

# Afficher le graphique
plt.show()


# 11 exercice 2

# Calcul de la moyenne glissante
moyennes = []

for i in range(len(notes) - 2):
    moyenne = (notes[i] + notes[i+1] + notes[i+2]) / 3
    moyennes.append(moyenne)

# Évaluations correspondant aux moyennes
evaluations_moyennes = evaluations[2:]

# Tracer les deux courbes
plt.plot(evaluations, notes, marker="o", label="Notes")
plt.plot(evaluations_moyennes, moyennes, marker="s",
         label="Moyenne glissante (3 évaluations)")

plt.title("Notes et moyenne glissante")
plt.xlabel("Évaluations")
plt.ylabel("Notes sur 20")

# Afficher la légende
plt.legend()

plt.show()