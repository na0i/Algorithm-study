import heapq
V, E = map(int, input().split())
start = int(input())
dist_list = [987654321] * (V+1)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

q = []
dist_list[start] = 0
heapq.heappush(q, (0, start))

while q:
    now_dist, now_node = heapq.heappop(q)
    if dist_list[now_node] < now_dist:
        continue

    for next in graph[now_node]:
        next_node = next[0]
        next_dist = next[1]

        if now_dist + next_dist < dist_list[next_node]:
            dist_list[next_node] = now_dist + next_dist
            heapq.heappush(q, (dist_list[next_node], next_node))

for d in range(1, V+1):
    if dist_list[d] == 987654321:
        print('INF')
    else:
        print(dist_list[d])

