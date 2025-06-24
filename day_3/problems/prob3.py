import random 
lst = []
for i in range(10) :
    rn=random.randint(10,50+1)
    lst.append(rn)
print(lst)
print(f"sum = {sum(lst)}")
