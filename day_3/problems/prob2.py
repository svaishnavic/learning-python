lst = [ "OK", "NOK" , "hello" , "hi" ]
#4
print(lst)
print(lst[-1])
print(lst[-2])
print(lst[0])
lst[-1] = "hello"
print(lst)

lst = [ "OK", "NOK" , "hello" , "hi" ]
#5
print(len(lst[1]))
#6
print(lst[:2])
print(lst[-2:])
#7
print(lst[::-1])
#8
print(lst[::2])
#9
for i in lst:
    print(i) 
#10
for i in lst:
    print(len(i))
    
    

