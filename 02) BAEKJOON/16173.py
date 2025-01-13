N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dr = [0, 1]
dc = [1, 0]
visited = [[0 for _ in range(N)] for _ in range(N)]
flag = False


def dfs(now_r, now_c):
    global flag

    if now_r == N - 1 and now_c == N - 1:
        flag = True
        return

    visited[now_r][now_c] = 1
    distance = board[now_r][now_c]
    next_dr = [r * distance for r in dr]
    next_dc = [c * distance for c in dc]

    for d in range(2):
        next_r = now_r + next_dr[d]
        next_c = now_c + next_dc[d]
        if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
            dfs(next_r, next_c)


dfs(0, 0)

if flag:
    print("HaruHaru")
else:
    print("Hing")
