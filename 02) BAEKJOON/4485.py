import sys
import heapq
tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    tc += 1
    INF = sys.maxsize
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cave = []
    for n in range(N):
        tmp = list(map(int, input().split()))
        cave.append(tmp)

    q = []
    heapq.heappush(q, ([0, 0], cave[0][0]))

    while q:
        now = heapq.heappop(q)
        now_r = now[0][0]
        now_c = now[0][1]
        now_cost = now[1]

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]

            if 0 <= next_r < N and 0 <= next_c < N:
                if dist[now_r][now_c] > dist[next_r][next_c]:
                    continue
                if now_cost + cave[next_r][next_c] < dist[next_r][next_c]:
                    dist[next_r][next_c] = now_cost + cave[next_r][next_c]
                    heapq.heappush(q, ([next_r, next_c], dist[next_r][next_c]))

    print('Problem', end=" ")
    print(tc, end=": ")
    print(dist[N-1][N-1])