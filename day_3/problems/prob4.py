lst = ["OK", "NOK", "hello", "hi"]
even_strlength = 0
odd_strlength = 0
lengths = []

for i in lst :
    length = len(i)
    if length %2 == 0 :
        even_strlength += 1
    else:   
        odd_strlength += 1
    total_strlength = sum(lengths)
print(f"num of even lengths = {even_strlength}")
print( f"num of odd lenghts = {odd_strlength}")
print(f"total length of all strings = {total_strlength}")

        
