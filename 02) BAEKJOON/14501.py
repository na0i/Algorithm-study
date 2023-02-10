N = int(input())
time = [0]
profits = [0]
for _ in range(N):
    t, profit = map(int, input().split())
    time.append(t)
    profits.append(profit)

dp = [0] * (N + 1)

for n in range(1, N + 1):
    end_time = time[n]
    now_profit = profits[n]

    dp[end_time] = dp[n - 1] + now_profit