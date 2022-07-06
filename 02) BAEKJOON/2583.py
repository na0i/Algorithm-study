M, N, K = map(int, input().split())
point_info = [list(map(int, input().split())) for _ in range(K)]
graph = [[0] * N for _ in range(M)]

for square in range(K):
    left_c = point_info[square][0]
    left_r = M - point_info[square][1] + 1
    right_c = point_info[square][2]
    right_r = M - point_info[square][3] + 1

    for i in range(right_r, left_r, -1):
        for j in range(right_c, left_c, -1):
            graph[i][j] = 1

    print(left_r, left_c, right_r, right_c)