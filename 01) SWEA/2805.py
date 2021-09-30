import sys
sys.stdin = open('2805.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    farm = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            farm[i][j] = int(farm[i][j])

    profit = 0
    row_idx = N//2
    col_idx = 0
    while col_idx < N and row_idx >= 0:
        profit += sum(farm[row_idx][col_idx:N - col_idx])
        col_idx += 1
        row_idx -= 1

    row_idx = N//2 + 1
    col_idx = 1
    while col_idx < N and row_idx < N:
        profit += sum(farm[row_idx][col_idx:N - col_idx])
        col_idx += 1
        row_idx += 1

    print('#{} {}'.format(tc+1, profit))