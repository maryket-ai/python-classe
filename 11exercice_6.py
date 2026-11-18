import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Créer les données des étudiants
donnees = {
    "Mathematiques": [10, 9, 11, 16, 15, 11, 7, 8, 5, 14],
    "Informatique": [14, 16, 11, 18, 17, 12, 19, 15, 18, 16],
    "Anglais": [10, 18, 13, 14, 11, 15, 16, 9, 14, 10]
}

# Construire le DataFrame
df = pd.DataFrame(donnees)
print(df)

# Calculer la matrice de corrélation
correlation = df.corr()
print(correlation)

# Créer la carte de chaleur
sns.heatmap(correlation, annot=True)

plt.title("Matrice de corrélation des notes")
plt.show()