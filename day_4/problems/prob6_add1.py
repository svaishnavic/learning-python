D1 = {'ok' : 1, 'nok' : 2}
D2 = {'ok' : 2, 'new' : 3}
D_UNION = {}
for i in D1.keys():
    D_UNION[i] = D1[i]
for i in D2.keys():
    if i not in D_UNION:
        D_UNION[i] = D2[i]
print("Union:" ,D_UNION)
D_INSERTION = {}
for i in D1.keys():
    if i in D2:
      D_INSERTION[i] = D1[i]
print("Intersection:" , D_INSERTION)
D_DIFF = {}
for i in D1.keys():
    if i not in D2:
        D_DIFF[i] = D1[i]
print("Difference:" , D_DIFF)
