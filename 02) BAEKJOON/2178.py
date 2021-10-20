def fastest(board, r, c):
    stack = [(r, c)]
    visited[r][c] = 1

    global result
    result = []

    while stack:
        now = stack.pop(0)
        result.append(now)
        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]

            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] == 0 and board[next_r][next_c] == 1:
                stack.append((next_r, next_c))
                # visted에 걸린 길이 적립
                visited[next_r][next_c] = visited[now[0]][now[1]] + 1

            if next_r == N-1 and next_c == M-1:
                return visited[N-1][M-1]


N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# miro 요소들 int 로
for i in range(N):
    for j in range(M):
        miro[i][j] = int(miro[i][j])


print(fastest(miro, 0, 0))