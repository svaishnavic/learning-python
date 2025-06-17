st = set()
print(st)
st = {1,2,3,6,3,3,2,4,5} #no repetion and in order for sets in the output
print(len(st))
#element existence
print( 4 in st)
#comapring sets
print(st == {4,5})
#iteration
for i in st:
    print(i)
for i in st:
    print(st)
#adding an element
st.add(8)
print(st)
#removes all the elements from the set
st.clear()
print(st)
#copying a set
st = {1,2,3,4,5} 
st_copy = st.copy() 
print(st_copy)
#removing an element
st.discard(2)
print(st)
#or
st.remove(4)
print(st)
popped =st.pop()
print(popped) #removed element
print(st) #set after removing an element
#updating a set
st.update({2,4})
print(st)
#intersection
st1= {1,2,3,4}
st2= {3,4,5,6}
intersect = st1.intersection(st2)
print(intersect) 
#difference 
diff = st2.difference(st1)
print(diff)
#prints elements that are not present in both simultaneously
symdiff= st1.symmetric_difference(st2)
print(symdiff)
st1={1,2,3}
st2= {4,5}
#all elemeents
u = st1.union(st2)
print(u)
#true if no elements in common
com= st1.isdisjoint(st2)
print(com)
# true if every element of one set is there in another
s= {1,2,3}
s1= {1,2,3,4}
ss= s.issubset(s1)
print(ss)



