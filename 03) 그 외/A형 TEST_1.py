import sys
sys.stdin = open('A형 TEST_1.txt', 'r')


def find_poe(pan):
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 2:
                r = i
                c = j
    return (r, c)


# 가로줄에 1이 얼마나 있는지
def check_one_row(row, start, end):
    cnt = 0
    for i in range(start, end):
        if board[row][i] == 1:
            cnt += 1

    return cnt


# 세로줄에 1이 얼마나 있는지
def check_one_col(col, start, end):
    cnt = 0
    for i in range(start, end):
        if board[i][col] == 1:
            cnt += 1

    return cnt


def next_position(pan, r, c):
    now_r = r
    now_c = c
    print(tc, '시작', now_r, now_c)

    global check, kill, up_le, down_r
    check += 1
    visited[now_r][now_c] = 1


    if check == 4:
        return kill

    if pan[now_r][now_c] == 1:
        kill += 1
        result.append((now_r, now_c))
        print(result)

    elif pan[now_r][now_c] == 0:
        kill += 0

    while 0 <= now_r + up_le < N and 0 <= now_c + down_r < N:

        for d in range(4):
            before_r = now_r + dr[d]
            before_c = now_c + dc[d]

            if 0 <= before_r < N and 0 <= before_c < N and pan[before_r][before_c] == 1:
                # 같은 세로줄에 대하여 위에 있을 경우
                if before_c == now_c and before_r < now_r:
                    for i in range(before_r):
                        if check_one_col(now_c, i, before_r) > 1:
                            return
                        else:
                            print(i, before_c)
                            if visited[i][before_c] == 0:
                                next_position(pan, i, before_c)

                # 같은 세로줄에 대하여 아래에 있을 경우
                elif before_c == now_c and before_r > now_r:
                    for i in range(before_r + 1, N):
                        if check_one_col(now_c, now_r, i) > 1:
                            return
                        else:
                            print(i, before_c)
                            if visited[i][before_c] == 0:
                                next_position(pan, i, before_c)

                # 같은 가로줄에 대해 왼쪽에 있을 경우
                elif before_r == now_r and before_c < now_c:
                    for j in range(before_c):
                        if check_one_row(now_r, j, before_c) > 1:
                            return
                        else:
                            print(before_r, j)
                            if visited[before_r][j] == 0:
                                next_position(pan, before_r, j)


                # 같은 가로줄에 대해 오른쪽에 있을 경우
                elif before_r == now_r and before_c > now_c:
                    for j in range(before_c + 1, N):
                        if check_one_row(now_r, now_c, j) > 1:
                            return
                        else:
                            print(before_r, j)
                            if visited[before_r][j] == 0:
                                next_position(pan, before_r, j)
        up_le -= 1
        down_r += 1


T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    poe_r = find_poe(board)[0]
    poe_c = find_poe(board)[1]

    up_le = -1
    down_r = 1
    dr = [up_le, down_r, 0, 0]
    dc = [0, 0, up_le, down_r]

    kill = 0
    check = 0
    result = []


    # (3, 2)
    # (5, 4)
    # (3, 6)
    # (19, 18)
    # (33, 40)

    next_position(board, poe_r, poe_c)
    print(kill)
    up_le = -1
    down_r = 1
    kill = 0
    check = 0
    result = []
    print()