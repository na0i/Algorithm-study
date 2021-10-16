N, M, V = map(int, input().split())

road = [[0] * (N+1) for _ in range(N+1)]
dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)
dfs_result = []
bfs_result = []


def DFS(board, s):
    dfs_visited[s] = 1
    dfs_result.append(s)

    for i in range(1, N+1):
        if dfs_visited[i] != 1 and board[s][i] == 1:
            DFS(board, i)


def BFS(board, s):
    stack = [s]
    bfs_visited[s] = 1
    bfs_result.append(s)

    while stack:
        now = stack.pop(0)

        for j in range(1, N+1):
            if bfs_visited[j] != 1 and board[now][j] == 1:
                stack.append(j)
                bfs_visited[j] = 1
                bfs_result.append(j)


for _ in range(M):
    start, end = map(int, input().split())
    road[start][end] = 1
    road[end][start] = 1

DFS(road, V)
BFS(road, V)

dfs_answer = ''
for i in range(len(dfs_result)):
    dfs_answer += str(dfs_result[i]) + ' '

bfs_answer = ''
for j in range(len(bfs_result)):
    bfs_answer += str(bfs_result[j]) + ' '

print(dfs_answer)
print(bfs_answer)