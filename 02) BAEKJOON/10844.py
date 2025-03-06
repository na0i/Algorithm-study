N = int(input())
dp = []

for i in range(N + 1):
    if i == 0:
        dp_0 = [0 for _ in range(10)]
        dp.append(dp_0)
    elif i == 1:
        dp_1 = [1 for _ in range(10)]
        dp_1[0] = 0
        dp.append(dp_1)
    else:
        dp_n = [0 for _ in range(10)]
        for j in range(10):
            if j == 0:
                dp_n[0] = dp[i - 1][1]
            elif j == 9:
                dp_n[9] = dp[i - 1][8]
            else:
                dp_n[j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp.append(dp_n)


print(sum(dp[N]) % 1000000000)