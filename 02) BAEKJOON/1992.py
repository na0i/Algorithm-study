N = int(input())
video = [list(input()) for _ in range(N)]


def check(lst):
    check_flag = True
    start_num = lst[0][0]

    for n in range(len(lst)):
        if lst[n] == start_num:
            continue
        else:
            check_flag = False
            break

    if check_flag:
        lst = start_num
    else:
        lst = lst

    return lst


size = N
if size > 2:
    while True:
        row_temp = []
        for row in range(2, size + 1, 2):
            col_temp = []
            for col in range(2, size + 1, 2):

                temp = []
                for i in range(row - 2, row):
                    for j in range(col - 2, col):
                        temp.append(video[i][j])

                temp = check(temp)
                col_temp.append(temp)
            row_temp.append(col_temp)

        size //= 2

        if size < 2:
            # video = row_temp
            break
        else:
            video = row_temp

else:
    temp = []
    for k in range(size):
        for l in range(size):
            temp.append(video[k][l])

    temp = check(temp)
    video = temp

# video = [[['1', '1', '0', ['0', '1', '0', '1']], ['0', '0', '1', '0']], ['1', ['0', '0', '0', '1']]]
video = str(video)

result = ''
if len(video) >= 3:
    for v in video:
        if v == '[':
            result += '('
        elif v == ']':
            result += ')'
        elif v == '0':
            result += str(v)
        elif v == '1':
            result += str(v)
        elif v == "'" or ',':
            continue

    print(result[1:-1])

else:
    result = '(' + video + ')'
    print(result)
