def calculer_moyenne_classe(classe):

    somme = 0

    for etudiant in classe:

        moyenne = (etudiant["note_cc"] * 0.4) + (etudiant["note_examen"] * 0.6)

        somme += moyenne

    moyenne_generale = somme / len(classe)

    return moyenne_generale


# Création de la classe
etudiants = [
    {"nom": "Marine", "note_cc": 15, "note_examen": 18},
    {"nom": "Sarah", "note_cc": 14, "note_examen": 15},
    {"nom": "David", "note_cc": 12, "note_examen": 15}
]

# Appel de la fonction
resultat = calculer_moyenne_classe(etudiants)

print(f"Moyenne générale de la classe : {resultat:.2f}")