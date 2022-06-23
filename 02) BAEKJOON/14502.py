N, M = map(int, input().split())
r, c, d = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def use_direction(direction):
    direction -= 1
    if direction < 0:
        direction = 3

    return direction


def clean(current_r, current_c, direction, cnt):
    print(current_r, current_c, direction, cnt)
    mapp[current_r][current_c] = 2

    if cnt >= 4:
        goback = direction - 2
        if goback < 0:
            goback += 4
        print('후진', current_r, current_c, goback, cnt)

        if mapp[current_r + dr[goback]][current_c + dc[goback]] == 1:
            return

        if mapp[current_r + dr[goback]][current_c + dc[goback]] != 1:
            back_r = current_r + dr[goback]
            back_c = current_c + dc[goback]
            clean(back_r, back_c, direction, 1)

    else:
        direction = use_direction(direction)
        next_r = current_r + dr[direction]
        next_c = current_c + dc[direction]

        if mapp[next_r][next_c] == 0:
            cnt += 1
            clean(next_r, next_c, direction, cnt)

        elif mapp[next_r][next_c] != 0:
            cnt += 1
            clean(current_r, current_c, direction, cnt)


clean(r, c, d, 0)
print(mapp)
answer = 0
for i in range(N):
    for j in range(M):
        if mapp[i][j] == 2:
            answer += 1

print(answer)