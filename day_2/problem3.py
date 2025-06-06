def prime_num(n):
    if n == 1 :
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True
    
for n in range(2,101):
    if prime_num(n):
        print(n)
