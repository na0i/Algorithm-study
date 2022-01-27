import sys
sys.stdin = open('1861.txt', 'r')


def change_room(curr_r, curr_c, cnt):
    for d in range(4):
        next_r = curr_r + dr[d]
        next_c = curr_c + dc[d]

        if 0 <= next_r < N and 0 <= next_c < N and rooms[curr_r][curr_c] + 1 == rooms[next_r][next_c]:
            print('여기')
            change_room(next_r, next_c, cnt + 1)


T = int(input())
for tc in range(T):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            print(change_room(i, j, 1))

