note_cc = [12.5, 14.0, 13.5, 16.0, 15.5] 
note_exam =[12, 15, 14, 15.5, 15.5]
i = 0
for i in range(0, len(note_cc)): 
    variation = note_exam[i] - note_cc[i - 1] 
    if variation <=0:
        print('note',i,'Pas de progression')
    else:
        print('note',i,'PROGRESSION')
        