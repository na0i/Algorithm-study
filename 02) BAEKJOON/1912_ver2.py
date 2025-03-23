N = int(input())
num_arr = list(map(int, input().split()))
dp = num_arr

now = 0

while now < N:
    if now == 0:
        now += 1
        continue
    else:
        if dp[now - 1] + num_arr[now] >= dp[now]:
            dp[now] = dp[now - 1] + num_arr[now]
            now += 1
        else:
            now += 1

print(max(dp))