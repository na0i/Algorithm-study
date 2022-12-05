heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
result = []
rows = len(heights)
cols = len(heights[0])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(rows):
    for c in range(cols):
        visited = [[0] * cols for _ in range(rows)]
        possible_P = False
        possible_A = False

        queue = [(r, c)]

        while queue:
            now = queue.pop()
            now_r = now[0]
            now_c = now[1]
            visited[now_r][now_c] = 1
            # print(now_r, now_c)

            for d in range(4):
                next_r = now_r + dr[d]
                next_c = now_c + dc[d]

                if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols or heights[next_r][next_c] > heights[now_r][now_c] or visited[next_r][next_c] == 1:
                    break


                else:
                    if next_r == 0 or next_c == 0:
                        possible_P = True
                    if next_r == rows or next_c == cols:
                        possible_A = True

                    queue.append((next_r, next_c))

            print(possible_P, possible_A)
            if possible_P and possible_A:
                result.append([next_r, next_c])
                break

print(result)