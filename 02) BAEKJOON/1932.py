N = int(input())
triangles = []
for _ in range(1, N+1):
    triangle = list(map(int, input().split()))
    triangles.append(triangle)

dp = [[triangles[0][0]]]

for i in range(1, N):
    temp = [dp[i-1][0] + triangles[i][0]]
    for j in range(1, i):
        temp.append(max(dp[i-1][j-1] + triangles[i][j], dp[i-1][j] + triangles[i][j]))
    temp.append(dp[i-1][-1] + triangles[i][-1])
    dp.append(temp)

print(max(dp[N-1]))
