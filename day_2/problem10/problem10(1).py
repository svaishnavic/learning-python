a = int(input("Give a value: "))
b = int(input("Give another value: "))
LHS = ( a + b)**2
RHS= ( a **2 + 2*a*b + b**2) 
if LHS == RHS :
    print(f"LHS:({a}+{b})**2={LHS}")
    print(f"RHS: ({a**2} + {2*a*b} + {b**2}) ={RHS}")
    print("Since LHS=RHS,Hence proven.")
