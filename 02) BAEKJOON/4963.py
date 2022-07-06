while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]


    def find_island(r, c):
        stack = [(r, c)]
        visited[r][c] = 1

        while stack:
            now = stack.pop()
            for d in range(8):
                next_r = now[0] + dr[d]
                next_c = now[1] + dc[d]
                if 0 <= next_r < h and 0 <= next_c < w and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 1:
                    visited[next_r][next_c] = 1
                    stack.append((next_r, next_c))


    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and graph[i][j] == 1:
                find_island(i, j)
                cnt += 1
    print(cnt)