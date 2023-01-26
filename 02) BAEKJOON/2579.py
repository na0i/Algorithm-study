N = int(input())
stairs = [0]
for _ in range(N):
    score = int(input())
    stairs.append(score)

dp = [0] * (N+1)
if N >= 2:
    dp[1] = stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N + 1):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

else:
    dp[-1] = stairs[-1]

print(dp[-1])