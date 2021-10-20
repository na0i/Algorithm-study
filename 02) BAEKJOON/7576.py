# deque가 시간 복잡도가 O(1)이고 pop(0)은 시간 복잡도가 O(n)이라고 한다.
# stack.pop으로 풀었더니 시간 초과가 났다.

from collections import deque


def riped_tomato():
    while queue:
        now = queue.popleft()
        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]

            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] == 0 and farm[next_r][next_c] == 0:
                queue.append((next_r, next_c))
                visited[next_r][next_c] = visited[now[0]][now[1]] + 1
                farm[next_r][next_c] = 1

    return farm


M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
riped = []
queue = deque()

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            queue.append([i, j])

riped_tomato()

flag = 1
date = 0
for i in range(N):
    for j in range(M):
        if farm[i][j] == 0:
            flag = -1
        if visited[i][j] > date:
            date = visited[i][j]

if flag == 1:
    print(date)
else:
    print(flag)