import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
M = int(input())

dists = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
start, end = map(int, input().split())

q = []
dists[start] = 0
heapq.heappush(q, (0, start))

while q:
    now = heapq.heappop(q)

    now_cost = now[0]
    now_node = now[1]

    if now_cost > dists[now_node]:
        continue

    for next in graph[now_node]:
        next_node = next[0]
        next_cost = next[1]

        if now_cost + next_cost < dists[next_node]:
            dists[next_node] = now_cost + next_cost
            heapq.heappush(q, (dists[next_node], next_node))

print(dists[end])
