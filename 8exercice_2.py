etudiants = [
    {"nom": "Marine", "note_cc": 15, "note_examen": 18},
    {"nom": "Sarah", "note_cc": 14, "note_examen": 15},
    {"nom": "David", "note_cc": 12, "note_examen": 15}
]
somme_moyennes = 0

for etudiant in etudiants:
    moyenne = (etudiant["note_cc"] * 0.4) + (etudiant["note_examen"] * 0.6)

    print(f"Nom : {etudiant['nom']}")
    print(f"Moyenne : {moyenne:.2f}")

    somme_moyennes += moyenne

moyenne_generale = somme_moyennes / len(etudiants)

print(f'Moyenne générale de la classe : {moyenne_generale:.2f}')