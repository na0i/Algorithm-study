from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
queue = deque()
result = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)


def tepology_sort():

    while queue:
        now = queue.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)


tepology_sort()
for i in result:
    print(i, end=' ')