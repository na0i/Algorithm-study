N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]

start_r = 0
start_c = 0
for i in range(N):
    for j in range(N):
        if room[i][j] == 9:
            start_r = i
            start_c = j
            room[i][j] = 0

# 상좌하우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def find_fish(now_r, now_c, eat, sec, shark_size):
    print(now_r, now_c, '먹었다', eat, '초', sec, '사이즈',shark_size)
    for d in range(4):
        next_r = now_r + dr[d]
        next_c = now_c + dc[d]

        if 0 <= next_r < N and 0 <= next_c < N:
            if room[next_r][next_c] > shark_size:
                print(next_r, next_c, '먹었다', eat, '내 크기', shark_size, '못가요')
                continue

            elif room[next_r][next_c] == 0:
                find_fish(next_r, next_c, eat, sec+1, shark_size)

            elif room[next_r][next_c] == shark_size:
                find_fish(next_r, next_c, eat, sec+1, shark_size)

            elif room[next_r][next_c] < shark_size:
                room[next_r][next_c] = 0
                eat += 1
                if eat == shark_size:
                    eat = 0
                    shark_size += 1
                find_fish(next_r, next_c, eat, sec+1, shark_size)
        else:
            continue


find_fish(start_r, start_c, 0, 1, 2)