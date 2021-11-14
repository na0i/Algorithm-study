import sys
sys.stdin = open('2806.txt', 'r')

def nqueen(row):
    global answer
    if row == N:
        answer += 1
        return

    # row = 지금 queen을 놓을 행
    # queen[c] = 비교할 queen이 있는 열
    # r = 지금 queen을 놓을 열
    # c = 비교할 queen이 있는 행
    for r in range(N):
        is_able = True

        for c in range(row):
            if r == queen[c] or abs(row - c) == abs(r - queen[c]):
                is_able = False
                break

        if is_able:
            queen[row] = r
            nqueen(row+1)
            queen[row] = -1


T = int(input())
for tc in range(T):
    N = int(input())
    answer = 0

    queen = [-1] * N
    nqueen(0)

    print('#{} {}'.format(tc+1, answer))