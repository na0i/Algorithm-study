import sys
sys.stdin = open('4615.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    # board setting
    board = list([0] * (N+1) for _ in range(N+1))
    board[N//2-1][N//2] = 2
    board[N//2-1][N//2+1] = 1
    board[N//2][N//2] = 1
    board[N//2][N//2+1] = 2

    for _ in range(M):
        row, col, color = map(int, input().split())

        # 왼위, 위, 오른위, 오른, 오른아래, 아래, 왼아래, 왼
        dr = [-2, -2, -2, 0, 2, 2, 2, 0]
        dc = [-2. 0, 2, 2, 2, 0, -2, -2]

        for dir in range(8):
            if 0 < row + dr[dir] < N and 0 < col + dc[dir] < N and board[row+dr[dir]][col+dc[dir]] == color:
                
