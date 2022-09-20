from copy import deepcopy
from collections import deque
N = int(input())
RGb_picture = [list(input()) for _ in range(N)]
not_RGb_picture = deepcopy(RGb_picture)
RGB_cnt = 0
not_RGB_cnt = 0
visited_RGB = [[0] * N for _ in range(N)]
visited_not_RGB = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for i in range(N):
    for j in range(N):
        if not_RGb_picture[i][j] == 'G':
            not_RGb_picture[i][j] = 'R'


def RGB(row, col, visited, picture, color):
    rgb_queue = deque()
    rgb_queue.append((row, col))

    while rgb_queue:
        now = rgb_queue.popleft()
        now_r = now[0]
        now_c = now[1]

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]

            if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == 0 and picture[next_r][next_c] == color:
                visited[next_r][next_c] = 1
                rgb_queue.append((next_r, next_c))


for i in range(N):
    for j in range(N):
        if visited_RGB[i][j] == 0:
            visited_RGB[i][j] = 1
            RGB_cnt += 1
            RGB(i, j, visited_RGB, RGb_picture,RGb_picture[i][j])
        if visited_not_RGB[i][j] == 0:
            visited_not_RGB[i][j] = 1
            not_RGB_cnt += 1
            RGB(i, j, visited_not_RGB, not_RGb_picture,not_RGb_picture[i][j])

print(RGB_cnt, end=' ')
print(not_RGB_cnt)