R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 1


def find_move_cnt(r, c):
    global cnt
    stack = [(r, c)]
    visited.append(graph[r][c])

    while stack:
        now = stack.pop()
        print(now)
        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]

            if 0 <= next_r < R and 0 <= next_c < C and graph[next_r][next_c] not in visited:
                stack.append((next_r, next_c))
                visited.append(graph[next_r][next_c])
                cnt += 1


find_move_cnt(0, 0)
print(cnt)
