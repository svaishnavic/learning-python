input = 'Name:ABC,age=20|Name:XYZ,age=30'
spliting = input.split('|')
print(spliting)
output= []
for i in spliting:
    p,q = i.split(':')
    r,s = q.split(',')
    output.append(f"{p}:{r.capitalize()},{s}")
result = '|'.join(output)
print(result)
