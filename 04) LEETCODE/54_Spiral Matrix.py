# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

rows = len(matrix)
cols = len(matrix[0])
visited = [[0] * cols for _ in range(rows)]
result = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d_idx = 0

current_r = 0
current_c = 0

while len(result) < rows * cols:
    result.append(matrix[current_r][current_c])
    visited[current_r][current_c] = 1

    next_r = current_r + dr[d_idx]
    next_c = current_c + dc[d_idx]

    if next_r == -1 or next_r == rows or next_c == -1 or next_c == cols or visited[next_r][next_c] == 1:
        d_idx += 1
        if d_idx == 4:
            d_idx = 0

        current_r += dr[d_idx]
        current_c += dc[d_idx]

    else:
        current_r = next_r
        current_c = next_c

print(result)