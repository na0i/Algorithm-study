import sys
sys.setrecursionlimit(100000)
N = int(input())
mmap = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
stack = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_height = 0
for i in range(N):
    for j in range(N):
        if mmap[i][j] >= max_height:
            max_height = mmap[i][j]


def find_safe_zone(r, c, height, graph):
    graph[r][c] = 1
    for d in range(4):
        next_r = r + dr[d]
        next_c = c + dc[d]

        if 0 <= next_r < N and 0 <= next_c < N and graph[next_r][next_c] == 0 and mmap[next_r][next_c] > height:
            find_safe_zone(next_r, next_c, height, graph)


safe_zone_cnt = []
for h in range(0, max_height):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and mmap[i][j] > h:
                cnt += 1
                find_safe_zone(i, j, h, visited)
    visited = [[0] * N for _ in range(N)]
    safe_zone_cnt.append(cnt)

print(max(safe_zone_cnt))
