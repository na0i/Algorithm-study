input_list = []
while True:
    nums = list(map(int, input().split()))
    if nums[0] == -1 and nums[1] == -1 and nums[2] == -1:
        break
    else:
        input_list.append(nums)

dp_list = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]


def dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    if dp_list[a][b][c]:
        return dp_list[a][b][c]
    if a < b < c:
        dp_list[a][b][c] = dp(a, b, c - 1) + dp(a, b - 1, c - 1) - dp(a, b - 1, c)
        return dp_list[a][b][c]
    else:
        dp_list[a][b][c] = dp(a - 1, b, c) + dp(a - 1, b - 1, c) + dp(a - 1, b, c - 1) - dp(a - 1, b - 1, c - 1)
        return dp_list[a][b][c]


for i in range(len(input_list)):
    x, y, z = map(int, input_list[i])
    print("w({}, {}, {}) = {}".format(x, y, z, dp(x, y, z)))