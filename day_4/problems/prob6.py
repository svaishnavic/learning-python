D1 = {'ok' : 1, 'nok' : 2}
D2 = {'ok' : 2, 'new' : 3}
for i in D1.keys()& D2.keys():
    D1[i] = D2[i] + D1[i]
D_MERGE = D2.copy()
D_MERGE.update(D1) 
print(D_MERGE)

