input = '[1,2,3,4]'
n = input.strip('[]')
parts = n.split(',')
l = []
for i in parts:
    l.append(int(i))
print(l)
