N = int(input())

dp = [0] * (N + 2)

dp[0] = 1
dp[1] = 1
dp[2] = 1
cnt_0 = 0
cnt_1 = 1

for i in range(2, N + 1):
    prev_0 = cnt_0
    prev_1 = cnt_1

    cnt_1 = prev_0
    cnt_0 = prev_0 + prev_1

    dp[i + 1] = 2 * cnt_0 + cnt_1

print(dp[N])