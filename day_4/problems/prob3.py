input = "ABCDEF1234567890"
pairs = zip(input[::2],input[1::2])
sum_total = 0
for a,b in pairs:
    hex_str = a + b
    num = int(hex_str,16)
    sum_total += num
print(sum_total)
check_sum = sum_total % 255
print(check_sum)