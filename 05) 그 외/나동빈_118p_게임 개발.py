import sys
sys.stdin = open('나동빈_118p_게임 개발.txt', 'r')

N, M = map(int, input().split())
c, r, direction = map(int, input().split())
mmap = [list(map(int, input().split())) for _ in range(M)]
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
cnt = 1

while True:
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < N and 0 <= next_c < M and mmap[next_r][next_c] == 0:
            r = next_r
            c = next_c
            mmap[next_r][next_c] = 1
            cnt += 1

            iz