dt = {}
print(dt)
dt = { 1:2, 'ok':3, 'k': 'no'}
#lenth
len(dt)
print( 'ok' in dt)
#comaparison
print( dt == {1:2})
#iteration over each element
for i in dt:
    print(i)
#iteration over whole dict
for i in dt:
    print(dt)
#creating a new key
dt[3] = 40
print(dt)
#accessing value given key list
print(dt['ok'])
#updating value of key
dt['k'] = 'yes'
print(dt)
#list of all keys in the dictionary
print(dt.keys())
#list of all the values
print(dt.values())
#list of tuples containing key-value pair
print(dt.items())
#gives value of specified key if exists, otherwise none
print(dt.get('k'))
print(dt.get(4))
