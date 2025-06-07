while True:
    c1 = input("Give one complex num:")
    c2 = input("Give one complex num:")
    operation = input("Give operation + - * / :")
    c1s = complex(c1.replace(" ",""))
    c2s = complex(c2.replace(" ",""))
    result = None 
    if operation == '+' :
        result = c1s + c2s
    elif operation == '-' :
        result = c1s - c2s
    elif operation == '*' :
        result = c1s*c2s
    elif operation == '/' :
        result = c1s/c2s
    else :
        print("operation not valid") 
    if result:
        print(f"result={result}")