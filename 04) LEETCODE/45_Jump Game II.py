nums = [2, 3, 1, 1, 4]
# nums = [2, 3, 0, 1, 4]
nums = [1, 1, 2, 2, 4, 2, 1]
min_jumps = [0] * len(nums)
now = 0

while min_jumps[-1] == 0 and now < len(nums):
    can_jump = now + nums[now]

    for i in range(now + 1, can_jump + 1):
        if i >= len(nums):
            break

        elif min_jumps[i]:
            min_jumps[i] = min(min_jumps[i], min_jumps[now] + 1)

        else:
            min_jumps[i] = min_jumps[now] + 1

    now += 1

print(min_jumps[-1])

