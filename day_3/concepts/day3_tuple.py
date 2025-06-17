tup = ()
print(tup)
tup = (1,2,3,4,5)
print(tup)
#lenth of tuple
print(len(tup))
#element existence
print( 2 in tup)
#comaparing
print(tup == (4,5))
#iteration of character over each other
for i in tup:
    print(i)
#iteration of whole set
for i in tup:
    print(tup)
#concatenation
print( tup + ( 7,8))
#accessing an element
print(tup[0])
print(tup[-2])
#slicing
print(tup[::3])
print(tup[1:4:2])
#updating not possible
tup = (1,2,3,4,5,2,6,4,3)
print(tup.count(3))
print(tup.index(5))


