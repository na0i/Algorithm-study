N = int(input())
board = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
stack = []
result = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0


def dfs():
    global cnt
    while stack:
        now = stack.pop()
        now_r = now[0]
        now_c = now[1]
        cnt += 1
        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == 0 and board[next_r][next_c] == "1":
                stack.append((next_r, next_c))
                visited[next_r][next_c] = 1


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and board[i][j] == "1":
            visited[i][j] = 1
            stack.append((i, j))
            dfs()
            if cnt != 0:
                result.append(cnt)
                cnt = 0

result = sorted(result)
print(len(result))
for i in range(len(result)):
    print(result[i])