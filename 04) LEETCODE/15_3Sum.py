from itertools import combinations

nums = [-15,13,6,-11,-4,5,-13,5,3,2,6,-1,4,12,-10,-13,-7,-4,-5,6,9,-14,1,-6,13,7,-8,10,-4,11,-8,-3,1,5,-7,4,-13,-13,-5,-3,4,-14,11,-14,5,-13,-12,13,-10,-10,-4,-15,13,13,-14,11,-3,-15,6,1,3,5,13,-11,-5,-9,1,-2,-14,11,10,5,4,-1,6,-6,-7,9,-15,-2,7,-12,-10,5,-14,13,-6,-9,6,7,7,-6,-2,-3,-9,0,-5,7,5,-4,-5,-7,-13,14,7,8,-15,7,-5,-15,-10,9]
triple_list = combinations(nums, 3)
temp_result = []
real_result = []

for i in triple_list:
    i = sorted(i)

    if sum(i) == 0:
        temp_result.append(i)

temp_result = sorted(temp_result)
real_result.append(temp_result[0])

for j in range(1, len(temp_result)):
    if temp_result[j] != temp_result[j-1]:
        real_result.append(temp_result[j])

print(real_result)
