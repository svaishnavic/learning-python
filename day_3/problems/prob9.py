sum_list = []
nums_list = []
for x in range(101):
    for y in range(x,101):
        for z in range(y, 101):
            if z*z == x*x + y*y :
                nums = (x , y , z)
                nums_list.append(nums)
                sum_list.append(x+y+z)
print(f"Pythogorus Triples-{nums_list}")
print(f"Sum-{sum_list}")
               
