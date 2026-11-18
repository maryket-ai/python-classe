etudiant = {
    "nom": "Amina",
    "age": 22,
    "filiere": "Informatique",
    "moyenne": 15.5
}

mention = etudiant.get("mention", "aucune")

print(f"Mention : {mention}")