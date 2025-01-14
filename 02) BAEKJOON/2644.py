from collections import deque

N = int(input())
A, B = map(int, input().split())
count = int(input())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(count):
    parent, child = map(int, input().split())
    graph[parent][child] = 1
    graph[child][parent] = 1

queue = deque([A])
visited = [A]
distance = [0 for _ in range(N + 1)]

while queue:
    v = queue.popleft()
    for j in range(1, N + 1):
        if j not in visited and graph[v][j] == 1:
            visited.append(j)
            queue.append(j)
            distance[j] = distance[v] + 1

            if j == B:
                break

if distance[B] == 0:
    print(-1)
else:
    print(distance[B])
