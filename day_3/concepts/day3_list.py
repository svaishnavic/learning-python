lst = []
print(lst)
lst=[1,2,3]
print(lst)
print(len(lst))
#existence of an element in list
print( 2 in lst)
#comparing two lists
print(lst == [1,2])
#iteration of each character
for i in lst:
    print(i)
#iteration as whole
for i in lst:
    print(lst)
#concatenation
lst2 = lst + [4,5]
print(lst2)
#adding an element to list
lst.append(6)
print(lst)
#accessing an element, postitive element
print(lst[0]) 
#negative element 
print(lst[-2])
#slicing
print(lst[::2])
print(lst[1:4:2])
#updating
lst[2] = "HELLO"
print(lst)
#extending the list
lst.extend([7,8,9])
print(lst)
#inserting a character at a particular index
lst.insert(2,"OK")
print(lst)
#removing an element
lst.remove("OK")
print(lst)
#removes and gives specified at index
lst.pop(2)
print(lst)
#clears the whole list
lst.clear()
print(lst)
lst = [1,2,3,8,5,2,6,7,4,9]
#counting the number of times an element occurs
print(lst.count(2))
#sorting in order
lst.sort()
print(lst)
lst.reverse()  #reverse of the order
print(lst)
#copying the lst
new_lst = lst.copy()
print(new_lst) 
#searching elements, returns index at which it is present
print(lst.index(7))

