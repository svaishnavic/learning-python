while True :
    float1= float(input("Give one number:"))
    float2 = float(input("Give another number:"))
    print(float1, float2)
    for i in range (10) :
        operation = input("Give operation: ")
        if operation == '+' :
            print(float1 + float2)  
        elif operation =='-' :
            print(float1 - float2)
        elif operation == '*' :
            print( float1*float2)
        elif operation == '/' :
            print( float1/float2)
        elif operation == "sqrt" :
            import math
            f1= float1 
            sf = math.sqrt(f1) 
            print(sf)
            f2= float2 
            sf1 = math.sqrt ( f2)
            print( sf1)
        elif operation == "exp" :
            import math
            f1= float1 
            ef = math.exp(f1) 
            print(ef)
            f2= float2 
            ef1 = math.exp( f2)
            print( ef1)
        elif operation == "sin" :
            import math 
            f1 = float1 
            sinf=math.sin(f1)
            print(sinf)
            f2 = float2
            sinf1=math.sin(f2)
            print(sinf1)
        elif operation == "cos" :
            import math 
            f1= float1 
            cf = math.cos(f1) 
            print(cf)
            f2= float2 
            cf1 = math.cos(f2)
            print( cf1)
        elif operation == "tan" :
            import math
            f1= float1
            tf = math.tan(f1)
            print(tf)
            f2= float2 
            tf1= math.tan(f2)
            print(tf1)
        elif operation == "log" :
            import math 
            f1 = float1
            lf = math.log(f1)
            print( lf)
            f2= float2 
            lf1= math.log( f2)
            print(lf1)
        else:
            print("Cannot perform operation")


            

                
                
