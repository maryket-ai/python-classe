notes = [8, 12, 15, 17, 10, 6] 
for note in notes:
    if note < 10 :
        print(note,': Echec')
    elif note >= 14:
        print(note,': Mention')
    else:
        print(note,': passable')
