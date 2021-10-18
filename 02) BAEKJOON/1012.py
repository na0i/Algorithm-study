# def find_baechu(ground, start_r, start_c):
#     visited[start_r][start_c] = 1
#     ground[start_r][start_c] = 0
#
#     for d in range(4):
#         next_r = start_r + dr[d]
#         next_c = start_c + dc[d]
#
#         if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] != 1 and ground[next_r][next_c] == 1:
#             find_baechu(ground, next_r, next_c)


def find_baechu(ground, start_r, start_c):
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = 1
    ground[start_r][start_c] = 0

    while stack:
        now = stack.pop(0)

        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]
            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] != 1 and ground[next_r][next_c] == 1:
                ground[next_r][next_c] = 0
                stack.append((next_r, next_c))


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    answer = 0

    for k in range(K):
        col, row = map(int, input().split())
        farm[row][col] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                find_baechu(farm, i, j)
                answer += 1

    print(answer)


# DFS로 푸니 런타임에러가 났다.
# 지나온 FARM을 0으로 바꿔주지 않아서 또 시간 초과가 났다.