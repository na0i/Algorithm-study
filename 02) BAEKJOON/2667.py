def find_apt(road, start_r, start_c):
    visited[start_r][start_c] = 1
    stack = [(start_r, start_c)]
    road[start_r][start_c] = 0
    cnt = 1

    while stack:
        now = stack.pop(0)
        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]

            if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] != 1 and road[next_r][next_c] == 1:
                visited[next_r][next_c] = 1
                stack.append((next_r, next_c))
                road[next_r][next_c] = 0
                cnt += 1
    return cnt


N = int(input())
town = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
all_cnt = []

for i in range(N):
    for j in range(N):
        town[i][j] = int(town[i][j])

for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            all_cnt.append(find_apt(town, i, j))
        else:
            continue

all_cnt = sorted(all_cnt)
print(len(all_cnt))

for c in range(len(all_cnt)):
    print(all_cnt[c])
