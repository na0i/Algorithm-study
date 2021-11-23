x, y, w, h = map(int, input().split())
square = [[0] * (w+1) for _ in range(h+1)]
visited = [[0] * (w+1) for _ in range(h+1)]
dist = [[0] * (w+1) for _ in range(h+1)]
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

def find_wall(map, r, c):
    visited[r][c] = 1
    stack = [(r, c)]

    while stack:

        now = stack.pop()
        now_r = now[0]
        now_c = now[1]

        for d in range(8):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]

            if 0 <= next_r <= h+1 and 0 <= next_c <= w+1 and visited[next_r][next_c] == 0:
                stack.append((next_r, next_c))
                visited[next_r][next_c] = 1
                dist[next_r][next_c] = dist[now_r][now_c] + 1

                if map[next_r][next_c] == 1:
                    return dist[next_r][next_c]

# making wall
for i in range(w+1):
    square[0][i] = 1
    square[h][i] = 1

for j in range(h+1):
    square[j][0] = 1
    square[j][w] = 1

answer = find_wall(square, y, x)
answer_list = [answer, x, y]
print(min(answer_list))