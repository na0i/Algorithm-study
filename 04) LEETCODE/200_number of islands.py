from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        cnt = 0

        def bfs(start_r, start_c):
            queue = deque()
            queue.append((start_r, start_c))
            visited[start_r][start_c] = 1

            while queue:
                now = queue.popleft()
                now_r = now[0]
                now_c = now[1]

                for d in range(4):
                    next_r = now_r + dr[d]
                    next_c = now_c + dc[d]

                    if 0 <= next_r < rows and 0 <= next_c < cols and visited[next_r][next_c] == 0 and grid[next_r][
                        next_c] == '1':
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = 1  # 방문체크 직후에 안해주면 시간초과 발생

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    bfs(i, j)
                    cnt += 1

        return cnt
