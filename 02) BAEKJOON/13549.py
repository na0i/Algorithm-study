import sys
import heapq
start, sister = map(int, input().split())
INF = sys.maxsize

costs = [INF for _ in range(100001)]
costs[start] = 0

move = ['prev', 'next', 'double']

q = []
heapq.heappush(q, (start, 0))

while q:
    now = heapq.heappop(q)
    now_point = now[0]
    now_cost = now[1]

    for m in move:
        if m == 'prev':
            next_point = now_point - 1
            next_cost = now_cost + 1
        elif m == 'next':
            next_point = now_point + 1
            next_cost = now_cost + 1
        elif m == 'double':
            next_point = now_point * 2
            next_cost = now_cost

        if 0 <= next_point <= 100000:
            if costs[next_point] < now_cost:
                continue

            if next_cost < costs[next_point]:
                costs[next_point] = next_cost
                heapq.heappush(q, (next_point, next_cost))

print(costs[sister])
