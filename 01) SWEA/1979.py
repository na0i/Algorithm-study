import sys
import copy

sys.stdin = open('1979.txt', 'r')


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    puzzle_row = [list(map(int, input().split())) for _ in range(N)]
    puzzle_col = copy.deepcopy(puzzle_row)

    possible = 0

    for i in range(N):
        for j in range(N):

            if puzzle_row[i][j] == 1:
                row_count = 0
                check_idx = j
                while check_idx < N and puzzle_row[i][check_idx] == 1:
                    row_count += 1
                    puzzle_row[i][check_idx] = 0
                    check_idx += 1

                if row_count == K:
                    possible += 1

    for i in range(N):
        for j in range(N):

            if puzzle_col[j][i] == 1:
                col_count = 0
                check_idx = j
                while check_idx < N and puzzle_col[check_idx][i] == 1:
                    col_count += 1
                    puzzle_col[check_idx][i] = 0
                    check_idx += 1

                if col_count == K:
                    possible += 1


    print('#{} {}'.format(tc+1, possible))