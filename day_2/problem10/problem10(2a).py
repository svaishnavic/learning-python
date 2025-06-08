a = int(input("Give a value: "))
b = int(input("Give another value: "))
LHS = ( a + b)**3
RHS= ( a **3 + 3*a*b*(a+b) + b**3) 
if LHS == RHS :
    print(f"LHS:({a}+{b})**3={LHS}")
    print(f"RHS: ({a**3} + {3*a*b*(a+b)} + {b**3}) ={RHS}")
    print("Since LHS=RHS,Hence proven.")

