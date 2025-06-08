a = int(input("Give a value: "))
b = int(input("Give another value: "))
LHS = ( a + b)**4
RHS= ( a**4 + 4*a**3*b + b**4 + 6*a**2*b**2 + 4*a*b**3) 
if LHS == RHS :
    print(f"LHS:({a}+{b})**3={LHS}")
    print(f"RHS: ({a**4} + {4*a**3*b} + {6*a**2*b**2} + {4*a*b**3} + {b**4}) ={RHS}")
    print("Since LHS=RHS,Hence proven.")

