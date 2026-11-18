def statistiques(notes):

    moyenne = sum(notes) / len(notes)

    minimum = min(notes)

    maximum = max(notes)

    return (moyenne, minimum, maximum)


# Liste des notes
notes = [12, 15, 8, 17, 10]

# Appel de la fonction
resultat = statistiques(notes)

print("Statistiques :", resultat)