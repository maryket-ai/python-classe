def mention(note, seuil_passable=10, seuil_bien=14):

    if note < seuil_passable:
        return "AJOURNÉ"

    elif note >= seuil_bien:
        return "BIEN"

    else:
        return "PASSABLE"


# Quelques tests
print(mention(8))
print(mention(12))
print(mention(16))