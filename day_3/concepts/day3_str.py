s = 'Hello' + " World" + """ and Hello Earth"""
print(s)
print('Hello World and \nHello \nEarth')
#raw strings
s2= r"/nHello"
print(s2)
print(len(s2)) #/n being treated as separate characters because of raw string.
name = "ABC"
age = 30
print(f"My name is {name} and age is {age}.")
x = 40
y = 38
print(f"Sum of x and y: {x + y}.")  #empty string
print("")
print(len(s)) #length of string
print( "He" in s) #substring existence 
a = "Hello"
print ( a == "Hello") #comparing str ( case sensitive)
print ( a == "hello")
for i in a : #iteration over each character
    print(i)
for i in a: #iteration for whole
    print(a) 
k = a + " world" #concatenation of two strings
print(k)
print(a[0])  #accessing an alphabet, positive indexing.
print(a[1])
print(a[2])
print( a[-1]) #negative indexing,from the back.
print(a[-2]) 
print(a[-3])
#slicing
print(a[0:3])
print(a[::2])
print(a[::-1]) #reversing string
#other methods
print("This is Vaishnavi".split())
#removing characters
print("        hi        ".strip()) 
print("I'm Vaishnavi".strip("I'm navi"))
#replacing substring with another
print("I'm Vaishnavi".replace("Vaishnavi", "ABCD")) 
#joining elements with a separator
print(":".join(["I'm", "Vaishnavi"]))
#uppercase and lowercase
print("hello".upper())
print("HeLlO".lower())
#checks start and end of substring
print("Vaishnavi".startswith("Vaish"))
print("Vaishnavi".endswith("navi"))
#gives index of substring
print("Vaishnavi".find("h"))
#gives -1 if index is not found
print("Vaishnavi".find("w"))
#number of times a substring is occuring
example= "red blue black red red pink red"
print(example.count("red"))
#checking what category the characters belong to
print("vaish29".isalnum()) #alphanumeric
print("vaish".isalpha()) #alphabetic
print("7468".isdigit()) #numeric
#aligning the strings with a character 
print("Hello".ljust(15,".")) #left
print("Hello".rjust(15,".")) #right
print( "Hello".center(15,".")) #center
#zeros to fill the string from left to a specified width
print("Hello".zfill(8))
#returns with first letter uppercase and lowercase the rest
print("hELLO".capitalize())
#lowercase entirely
print("HELLO".casefold())
#formatting
name = "ABCD"
age = 24
format = "Name: {}, Age: {}".format(name,age)
print(format)



