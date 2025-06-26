d = { "me" : [200,300] , "you" : [400,1,2]}
print(d)
print(type(d["you"]))
for i in d:
    print(len(d[i]))
print(len(d["me"]))
d["me"].extend([20,30])
print(d)
sum = 0
for i in d["me"]:
    sum += i
print(sum)
sum1 = 0
for i in d["you"]:
    sum1+= i
print(sum1)
print(f" required sum of 'me' : { sum +len(d["me"])}")
print(f" required sum of 'you': {sum1+ len ( d[ "you" ] )}")