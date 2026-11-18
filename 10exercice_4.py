def calculer_moyenne(note_cc, note_examen):
    moyenne = (note_cc * 0.4) + (note_examen * 0.6)
    return moyenne


# Calcul des moyennes
moyenne_amina = calculer_moyenne(15.5, 16)
moyenne_paul = calculer_moyenne(12, 13.5)
moyenne_sarah = calculer_moyenne(16, 18)

# Affichage des résultats
print("Moyenne d'Amina :", moyenne_amina)
print("Moyenne de Paul :", moyenne_paul)
print("Moyenne de Sarah :", moyenne_sarah)