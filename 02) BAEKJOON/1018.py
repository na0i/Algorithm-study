# def make_chess(r, c):
#     global ori_cnt, rev_cnt
#     ori_cnt = 0
#     rev_cnt = 0
#
#     # (짝수, 짝수)나 (홀수, 홀수)가 시작점일 경우
#     # (짝수, 짝수) 혹은 (홀수, 홀수)는 시작점과 같고
#     # (짝수, 홀수) 혹은 (홀수, 짝수)는 시작점과 달라야한다.
#     if r % 2 == c % 2:
#         for i in range(r, r + 8):
#             for j in range(c, c + 8):
#                 if i % 2 == j % 2 and board[i][j] != board[r][c]:
#                     ori_cnt += 1
#                 elif i % 2 != j % 2 and board[i][j] == board[r][c]:
#                     ori_cnt += 1
#
#         # 끝점으로부터도 확인해본다.
#         for k in range(r + 7, r - 1, -1):
#             for l in range(c + 7, c - 1, -1):
#                 if k % 2 == l % 2 and board[k][l] != board[r+7][c+7]:
#                     rev_cnt += 1
#                 elif k % 2 != l % 2 and board[k][l] == board[r+7][c+7]:
#                     rev_cnt += 1
#
#     else:
#         for i in range(r, r + 8):
#             for j in range(c, c + 8):
#                 if i % 2 == j % 2 and board[i][j] == board[r][c]:
#                     ori_cnt += 1
#                 elif i % 2 != j % 2 and board[i][j] != board[r][c]:
#                     ori_cnt += 1
#
#         for k in range(r + 7, r - 1, -1):
#             for l in range(c + 7, c - 1, -1):
#                 if k % 2 == l % 2 and board[k][l] == board[r+7][c+7]:
#                     rev_cnt += 1
#                 elif k % 2 != l % 2 and board[k][l] != board[r+7][c+7]:
#                     rev_cnt += 1
#
#     if ori_cnt < rev_cnt:
#         return ori_cnt
#     else:
#         return rev_cnt
#
#
# N, M = map(int, input().split())
# board = [list(input()) for _ in range(N)]
# result = []
#
# for n in range(N - 8 + 1):
#     for m in range(M - 8 + 1):
#         result.append(make_chess(n, m))
#
# print(min(result))


def check_bw(r, c):
    b_cnt = 0
    w_cnt = 0
    standard_b = 'B'
    standard_w = 'W'

    for k in range(r, r+8):
        for l in range(c, c+8):
            if (k + l) % 2 == (r + c) % 2:
                if standard_b != board[k][l]:
                    b_cnt += 1
            else:
                if standard_b == board[k][l]:
                    b_cnt += 1

    for m in range(r, r+8):
        for n in range(c, c+8):
            if (m + n) % 2 == (r + c) % 2:
                if standard_w != board[m][n]:
                    w_cnt += 1
            else:
                if standard_w == board[m][n]:
                    w_cnt += 1

    if b_cnt <= w_cnt:
        return b_cnt
    else:
        return w_cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
temp = []

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        temp.append(check_bw(i, j))

print(min(temp))
