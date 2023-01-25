N = int(input())
dp = [0] * (N + 1)

for n in range(2, N + 1):
    temp = []
    if n % 3 == 0:
        temp.append(dp[n // 3])
    if n % 2 == 0:
        temp.append(dp[n // 2])
    if n - 1 >= 0:
        temp.append(dp[n - 1])

    dp[n] = min(temp) + 1

print(dp[N])