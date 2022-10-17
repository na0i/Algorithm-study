n = 5
k = 73

z_cnt = (k-n) // 26

a_cnt = n - z_cnt
mid_num = k - (z_cnt * 26) - (a_cnt - 1)
num_arr = ([1] * (a_cnt - 1)) + [mid_num] + ([26] * z_cnt)

# 반례: [1, 1, 1, 29, 26, 26, 26] 등장하는 상황 방지
for i in range(len(num_arr)-1, -1, -1):
    if num_arr[i] > 26:
        num_arr[i-1] = num_arr[i] - 25
        num_arr[i] = 26

answer = ''
for num in num_arr:
    answer += chr(num + 96)

print(answer)