import cmath 
while True :
    c1 =input("Give one number: ")
    c2 =input("Give another number: ")
    c1 = c1.replace(" ","")
    c2 = c2.replace(" ","")
    c1s= complex(c1)
    c2s=complex(c2)
    operation = input("Give an operation:")
    if operation == '+' :
        print(c1s + c2s)  
    elif operation == '-' :
        print(c1s - c2s)
    elif operation == '*' :
        print( c1s*c2s)
    elif operation == '/' :
        print( c1s/c2s)
    elif operation == "sqrt" :
        print(cmath.sqrt(c1s)) 
        print(cmath.sqrt (c2s))
    elif operation == "exp" :
        print(cmath.exp(c1s)) 
        print(cmath.exp(c2s))
    elif operation == "log" :
        print(cmath.log(c1s)) 
        print(cmath.log(c2s))
    elif operation == "sin" :
        print(cmath.sin(c1s)) 
        print(cmath.sin(c2s))
    elif operation == "cos" :
        print(cmath.cos(c1s)) 
        print(cmath.cos(c2s))
    elif operation == "tan" :
        print(cmath.tan(c1s)) 
        print(cmath.tan(c2s))
    
        