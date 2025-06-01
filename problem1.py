import random
float1= random.random() 
float2 = random.random()
print(float1, float2)
print("Choose one operation: + - * /")
operation = input("Give operation: ")
if operation == '+' :
    print(float1 + float2)  
operation = input("Give operation: ")
if operation == '-' :
    print(float1 - float2) 
operation = input("Give operation: ")
if operation == '*' :
    print( float1 * float2)
operation = input("Give operation: ")
if operation == '/' :
    print( float1/float2) 
 


