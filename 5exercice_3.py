note = 40 
progression_hebdo = 0.03   # 3 % par semaine
semaine = 0 
objectif = 60 
while note < objectif: 
    note = note * (1 + progression_hebdo) 
    semaine = semaine + 1 
print(f"Objectif atteint après {semaine} semaines, note finale : {note:.2f}") 
