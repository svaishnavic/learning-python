triples = {}
for x in range(101):
    for y in range(x,101):
        for z in range(y, 101):
            if z*z == x*x + y*y :
                triples[(x,y,z)] = sum((x,y,z))
for num,total in triples.items():
    print(f"{num} = {total}")
