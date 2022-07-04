N, M = map(int, input().split())
r, c, d = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


def turn_back(direction):
    direction -= 2
    if direction <= -1:
        direction += 4
    return direction


turn_cnt = 0
answer = 1
while True:
    next_d = turn_left(d)
    next_r = r + dr[next_d]
    next_c = c + dc[next_d]

    if visited[next_r][next_c] == 0 and mapp[next_r][next_c] == 0:
        visited[next_r][next_c] = 1
        r = next_r
        c = next_c
        d = next_d
        turn_cnt = 0
        answer += 1

    else:
        d = next_d
        turn_cnt += 1

    if turn_cnt == 4:
        back_d = turn_back(d)
        back_r = r + dr[back_d]
        back_c = c + dc[back_d]
        if mapp[back_r][back_c] == 0:
            r = back_r
            c = back_c
            turn_cnt = 0

        else:
            break

print(answer)