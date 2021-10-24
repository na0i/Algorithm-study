from collections import deque
import sys
sys.stdin = open('10966.txt', 'r')


def bfs():
    visited[myqueue[0][0]][myqueue[0][1]] = 1

    while myqueue:
        now = myqueue.popleft()

        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]

            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] == 0:
                myqueue.append((next_r, next_c))
                visited[next_r][next_c] = 1
                dist[next_r][next_c] = dist[now[0]][now[1]] + 1

    return dist

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    pool = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dist = [[0] * M for _ in range(N)]
    myqueue = deque()
    W_list = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                myqueue.append((i, j))
                visited[i][j] = 1

    bfs()

    ans = 0
    for i in range(N):
        for j in range(M):
            ans += dist[i][j]

    print('#{} {}'.format(tc+1, ans))

# Land에서 Water를 찾으면 시간초과가 났다.
# 반대로 Water에서 Land를 찾는식으로 코드를 짠다.
# BFS를 이용한다.
# deque를 이용하는 것이 시간복잡도에서 유리하다.
