import matplotlib.pyplot as plt
import seaborn as sns

notes = [12, 14, 12, 15, 16, 13, 17, 10, 18, 9,
         12, 14, 16, 10, 8, 13, 14, 17, 11, 14]

# Créer l'histogramme
sns.histplot(notes, bins=5, kde=True)

plt.title("Distribution des notes des étudiants")
plt.xlabel("Notes")
plt.ylabel("Nombre d'étudiants")

plt.show()