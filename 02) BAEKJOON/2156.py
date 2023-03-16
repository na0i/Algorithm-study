N = int(input())
wine_list = []
for _ in range(N):
    wine_list.append(int(input()))

dp = [0] * N

if N == 1:
    print(wine_list[0])
elif N == 2:
    print(wine_list[0] + wine_list[1])

else:
    dp[0] = wine_list[0]
    dp[1] = wine_list[0] + wine_list[1]
    dp[2] = max(wine_list[0] + wine_list[1], wine_list[1] + wine_list[2], wine_list[0] + wine_list[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + wine_list[i], dp[i-3] + wine_list[i-1] + wine_list[i], dp[i-1])

    print(dp[N-1])