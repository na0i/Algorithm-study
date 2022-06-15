import sys
sys.stdin = open('나동빈_153p_미로 탈출.txt', 'r')
from collections import deque

N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]
start_r = 0
start_c = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = []

queue = deque()
queue.append((start_r, start_c))
distance = 1

while queue:
    current_r, current_c = queue.popleft()
    visited.append((current_r, current_c))
    for d in range(4):
        next_r = current_r + dr[d]
        next_c = current_c + dc[d]

        if next_r == N - 1 and next_c == M - 1:
            break

        elif (next_r, next_c) in visited and miro[next_r][next_c] == '1':
            distance -= 1

        elif 0 <= next_r < N and 0 <= next_c < M and miro[next_r][next_c] == '1':
            queue.append((next_r, next_c))
            miro[next_r][next_c] = '0'
            distance += 1

print(distance)