import sys
sys.stdin = open('나동빈_110p_상하좌우.txt', 'r')

N = int(input())
path = list(map(str, input().split()))
move_cnt = len(path)
mmap = [[0] * N for _ in range(N)]
current_r = 0
current_c = 0

for i in range(move_cnt):
    if path[i] == 'L' and 0 <= current_c - 1 < N:
        current_c -= 1
    elif path[i] == 'R' and 0 <= current_c + 1 < N:
        current_c += 1
    elif path[i] == 'U' and 0 <= current_r - 1 < N:
        current_r -= 1
    elif path[i] == 'D' and 0 <= current_r + 1 < N:
        current_r += 1

print(current_r+1, current_c+1)