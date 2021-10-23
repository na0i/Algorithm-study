import sys
sys.stdin = open('10966.txt', 'r')

from collections import deque

def bfs(r, c):
    myqueue.append((r, c))
    visited[r][c] = 1
    dist[r][c] = 0

    while myqueue:
        now = myqueue.popleft()

        if land[now[0]][now[1]] == 'W':
            print(r, c, dist[now[0]][now[1]])
            print(dist)
            break

        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]

            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] == 0:
                myqueue.append((next_r, next_c))
                visited[next_r][next_c] = 1
                dist[next_r][next_c] = dist[now[0]][now[1]] + 1


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    land = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dist = [[0] * M for _ in range(N)]
    myqueue = deque()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if land[i][j] == 'L':
                bfs(i, j)
                visited = [[0] * M for _ in range(N)]
                dist = [[0] * M for _ in range(N)]

    print()