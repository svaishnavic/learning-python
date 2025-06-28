sum = {}
for x in range(101):
    for y in range(x,101):
        for z in range(y, 101):
            if z*z == x*x + y*y :
                sum[(x,y,z)] = x+y+z
for num,total in sum.items():
    print(f"{num} = {total}")
