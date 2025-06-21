s = [1,2,3,4]
s1 = []
for i in s:
    if i not in s1 and i%2 != 0:
        s1.append(i*i)
print(s1)
