N = int(input())
num_list = list(map(int, input().split()))
dp = [-1000] * N
dp[0] = num_list[0]

for i in range(1, N):
    if dp[i - 1] + num_list[i] > num_list[i]:
        dp[i] = dp[i - 1] + num_list[i]
    else:
        dp[i] = num_list[i]

print(max(dp))