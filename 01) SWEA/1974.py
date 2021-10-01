import sys
sys.stdin = open('1974.txt', 'r')

T = int(input())
for tc in range(T):
    board = [list(map(int, input().split())) for _ in range(9)]

    def row_check():
        for i in range(9):
            check = [0] * 10
            for j in range(9):
                check[board[i][j]] = 1

            if check[1: 10] != [1] * 9:
                return False
        return True

    def col_check():
        for i in range(9):
            check = [0] * 10
            for j in range(9):
                check[board[j][i]] = 1

            if check[1: 10] != [1] * 9:
                return False
        return True

    def box_check():
        idx = 3
        while idx <= 9:
            check = [0] * 10

            for i in range(idx-3, idx):
                for j in range(idx-3, idx):
                    check[board[i][j]] = 1

            if check[1: 10] != [1] * 9:
                return False

            idx += 3
        return True

    if row_check() and col_check() and box_check():
        print('#{} {}'.format(tc+1, 1))

    else:
        print('#{} {}'.format(tc+1, 0))