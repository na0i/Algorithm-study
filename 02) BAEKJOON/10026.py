import copy
import sys
sys.setrecursionlimit(100000)
N = int(input())
picture = [list(input()) for _ in range(N)]
visited_1 = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]
stack_1 = []
stack_2 = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


rg_picture = copy.deepcopy(picture)
for i in range(N):
    for j in range(N):
        if rg_picture[i][j] == 'G':
            rg_picture[i][j] = 'R'


def not_color_weakness(r, c, color, graph, visit_arr):
    visit_arr[r][c] = 1

    for d in range(4):
        next_r = r + dr[d]
        next_c = c + dc[d]

        if 0 <= next_r < N and 0 <= next_c < N and visit_arr[next_r][next_c] == 0 and color == graph[next_r][next_c]:
            not_color_weakness(next_r, next_c, color, graph, visit_arr)


color_weakness_cnt = 0
not_color_weakness_cnt = 0
for i in range(N):
    for j in range(N):
        if visited_1[i][j] == 0:
            not_color_weakness(i, j, rg_picture[i][j], rg_picture, visited_1)
            color_weakness_cnt += 1
        if visited_2[i][j] == 0:
            not_color_weakness(i, j, picture[i][j], picture, visited_2)
            not_color_weakness_cnt += 1


print(not_color_weakness_cnt, color_weakness_cnt)