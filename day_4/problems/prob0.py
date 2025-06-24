s = {1,2,3}
if s =={3,2,1}:
    print("same")
else:
    print("no-same")
print(len(s))
if 30 not in s:
    print("not-part")
print(list(s)[0])
s1 = {i+10 for i in s} 
print(s1)