import sys
sys.stdin = open('4836.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    board = [([0] * 10) for _ in range(10)]
    answer = 0

    for n in range(N):
        color = list(map(int, input().split()))

        for i in range(color[0], color[2]+1):
            for j in range(color[1], color[3]+1):
                board[i][j] += color[4]
                if board[i][j] == 3:
                    answer += 1

    print('#{} {}'.format(tc+1, answer))