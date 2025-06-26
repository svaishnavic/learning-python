input = '[1,2,3,4]'
n = input.strip('[]')
l = n.split(',')
for i in range(len(l)):
    l[i] = int(l[i])
print(l)
