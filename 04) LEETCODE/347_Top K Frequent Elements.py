nums = [1,1,1,2,2,3]
k = 2

nums = sorted(nums)

cnt_list = []
temp = []
start = nums[0]

for num in nums:
    if num == start:
        temp.append(num)
    else:
        cnt_list.append(temp)
        temp = [num]
        start = num

cnt_list.append(temp)

cnt_list = sorted(cnt_list, key=lambda x: len(x), reverse=True)[:k]

answer = []
for i in range(k):
    answer.append(cnt_list[i][0])

print(answer)