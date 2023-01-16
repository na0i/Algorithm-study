nums = [0, 1, 5, 0, 3, 5, 6, 7]
nums.sort()
cnt = 0
acc_subtract = 0

for num in nums:
    subtracted_num = num - acc_subtract

    if subtracted_num == 0:
        continue
    else:
        acc_subtract += subtracted_num
        cnt += 1

print(cnt)