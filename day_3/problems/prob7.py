input_str = "Hello world and Hello Earth"
words=input_str.split()
unique = list(set(words))
for i in unique:
    count = words.count(i)
    print(f"{i}-{count}")
    
    

    