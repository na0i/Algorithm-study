isConnected = [[1,0,0],[0,1,0],[0,0,1]]
N = len(isConnected)
visited = [0] * N
answer = 0


def dfs(now):
    for next in range(N):
        if isConnected[now][next] == 1 and visited[next] == 0 and now != next:
            visited[next] = 1
            dfs(next)


for row in range(N):
    if visited[row] == 0:
        dfs(row)
        answer += 1


print(visited, answer)