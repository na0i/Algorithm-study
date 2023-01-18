N, M = map(int, input().split())
edges_list = [list(map(int, input().split())) for _ in range(M)]
link_list = [[] for _ in range(N + 1)]
visited = [False for _ in range(N+1)]

for edge in edges_list:
    start = edge[0]
    end = edge[1]
    link_list[start].append(end)
    link_list[end].append(start)


def dfs(now):
    visited[now] = True

    for next in link_list[now]:
        if visited[next] == False:
            dfs(next)


answer = 0
for link in link_list:
    for l in link:
        if not visited[l]:
            dfs(l)
            answer += 1

print(answer + visited.count(False) - 1)

