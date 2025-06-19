import random 
lst = []
sum_numbers = 0
for i in range(10) :
    rn=random.randint(10,50+1)
    lst.append(rn)
    sum_numbers += rn
print(lst)
print(f"sum = {sum_numbers}")