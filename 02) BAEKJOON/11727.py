N = int(input())
if N == 1:
    print(1)

elif N == 2:
    print(3)

else:
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    start = 4

    while start <= N:
        dp[start] = 2 * dp[start - 2] + dp[start - 1]
        start += 1

    print(dp[-1] % 10007)
