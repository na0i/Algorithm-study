import sys
sys.stdin = open('과목평가복습_문제1.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mmap = [list(map(int, input().split())) for _ in range(N)]
    bomb = [list(map(int, input().split())) for _ in range(M)]

    dr = [-1, 1, -1, 1]
    dc = [-1, -1, 1, 1]

    answer = 0
    for b in range(M):
        now_r = bomb[b][0]
        now_c = bomb[b][1]
        answer += mmap[now_r][now_c]
        mmap[now_r][now_c] = 0

        for i in range(1, bomb[b][2]+1):
            for dir in range(4):
                next_r = now_r + (dr[dir] * i)
                next_c = now_c + (dc[dir] * i)

                if 0 <= next_r < N and 0 <= next_c < N:
                    answer += mmap[next_r][next_c]
                    mmap[next_r][next_c] = 0
    print(answer)