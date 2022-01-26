import sys
sys.stdin = open('2819.txt', 'r')


def make_num(curr_r, curr_c, number, turn):
    global num, answer

    # 이부분 있으면 제한시간 초과
    # 자꾸 돌아가면서 시간이 초과되나..?
    # if turn == 7 and len(number) == 7 and number in answer:
    #     return

    if turn == 7 and len(number) >= 7 and number not in answer:
        answer.append(number)
        return

    if turn <= 6:
        for d in range(4):
            next_r = curr_r + dr[d]
            next_c = curr_c + dc[d]

            if 0 <= next_r < 4 and 0 <= next_c < 4:
                number += board[next_r][next_c]
                turn += 1
                make_num(next_r, next_c, number, turn)
                turn -= 1
                number = number[:-1]


T = int(input())
for tc in range(T):
    board = [list(map(str, input().split())) for _ in range(4)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    answer = []
    num = ''

    for i in range(4):
        for j in range(4):
            make_num(i, j, num, 0)

    print('#{} {}'.format(tc+1, len(set(answer))))