N = int(input())
dp = [0] * N

if N > 2:
    dp[1] = 2
    dp[2] = 3
    start = 3
    while start < N:
        dp[start] = dp[start-1] + dp[start-2]
        start += 1

    print(dp[N-1] % 10007)

else:
    print(N)