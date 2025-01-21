M, N, K = map(int, input().split())
graph_paper = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, input().split())
    left_r = M - right_y
    left_c = left_x
    right_r = M - left_y
    right_c = right_x

    for row in range(left_r, right_r):
        for col in range(left_c, right_c):
            graph_paper[row][col] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# Python은 기본적으로 최대 재귀 깊이가 약 1000으로 제한
# DFS를 재귀로 구현할 경우, 깊은 탐색을 수행하면 재귀 깊이가 이 한도를 초과하여 RecursionError가 발생
# def dfs(now):
#     global width
#     now_r = now[0]
#     now_c = now[1]
#     visited[now_r][now_c] = True
#     width += 1
#
#     for d in range(4):
#         next_r = now_r + dr[d]
#         next_c = now_c + dc[d]
#
#         if 0 <= next_r < M and 0 <= next_c < N and not visited[next_r][next_c] and graph_paper[next_r][next_c] == 0:
#             dfs([next_r, next_c])


section = 0
section_width = []
for i in range(M):
    for j in range(N):
        if graph_paper[i][j] == 0 and not visited[i][j]:
            stack = [[i, j]]
            width = 0

            while stack:
                now = stack.pop()
                now_r = now[0]
                now_c = now[1]

                if not visited[now_r][now_c]:
                    visited[now_r][now_c] = True
                    width += 1

                    for d in range(4):
                        next_r = now_r + dr[d]
                        next_c = now_c + dc[d]

                        if 0 <= next_r < M and 0 <= next_c < N and not visited[next_r][next_c] and graph_paper[next_r][next_c] == 0:
                            stack.append([next_r, next_c])

            section += 1
            section_width.append(width)

print(section)
print(" ".join(map(str, sorted(section_width))))