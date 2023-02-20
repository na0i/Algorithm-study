import heapq
N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dist_list = [300000] * (N+1)
for m in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)


q = []
heapq.heappush(q, start)
dist_list[start] = 0

while q:
    now_node = heapq.heappop(q)

    for next_node in graph[now_node]:
        if dist_list[now_node] + 1 < dist_list[next_node]:
            dist_list[next_node] = dist_list[now_node] + 1
            heapq.heappush(q, next_node)

is_exist = False
for k in range(1, N+1):
    if dist_list[k] == K:
        is_exist = True
        print(k)

if not is_exist:
    print(-1)

# 시간 초과 코드
# dist[start] = 0
# visited[start] = True
# for i in graph[start]:
#     dist[i] = 1
#
# for now_node in range(1, N+1):
#
#     closest_dist = 987654321
#     closest_node = 987654321
#     for i in range(1, N+1):
#         if not visited[i] and dist[i] < closest_dist:
#             closest_dist = dist[i]
#             closest_node = i
#
#     if closest_node == 987654321:
#         break
#     else:
#         visited[closest_node] = True
#
#         for next_node in graph[closest_node]:
#             if dist[closest_node] + 1 < dist[next_node]:
#                 dist[next_node] = dist[closest_node] + 1
#
#
# is_exist = False
# for k in range(1, N+1):
#     if dist[k] == K:
#         is_exist = True
#         print(k)
#
# if not is_exist:
#     print(-1)