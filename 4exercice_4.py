etudiant = [ 
    ["Kassandra", 19, 14.5], 
    ["Prince", 21, 12.0], 
    ["Alain", 20, 16.5], 
] 

print('le deuxieme nom dans la liste:',etudiant[1][0])
note1 = etudiant[0][2]
note2 = etudiant[1][2]
note3 = etudiant[2][2]
moy = (note1+note2+note3)/3
print(f'la moyenne des etudiant est:{moy:.2f}')
