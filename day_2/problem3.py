for n in range(1,101):
    if n > 1 :
        prime = True
        for i in range ( 2, n):
            if (n % i) == 0:
                prime = False
                break
        if prime:
            print(n)