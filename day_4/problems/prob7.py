input_str = "Hello world and Hello Earth"
frequency = {}
for i in input_str.split():
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
for i, frequency in frequency.items():
    print(f"{i} - {frequency}")
