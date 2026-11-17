nom = 'Toma'
note = [12.5, 10, 14.5, 13, 17, 13]
print('les notes de',nom,':',note)
print('la premiere note:',note[0])
print('la derniere note:',note[-1])
print('les trois dernieres notes:',note[-3:])
#4 exercice 2
basse = min(note) 
haute = max(note) 
moyenne = sum(note) / len(note) 
print(f"Plus basse : {basse} — Plus haute : {haute} — Moyenne : {moyenne:.2f}") 
# 4 exercice 3
note.append(14.0)   
print('Ajout en fin de liste:',note)
note.pop(0)
print('suppression note indice 0:',note) 