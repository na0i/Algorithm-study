N = int(input())
visited = [0] * N
answer = 0
row = 0


def check(now_r, now_c, prev_r, prev_c):
    flag = True
    if now_r - prev_r == 1 and now_c - prev_c == 1:
        flag = False
    elif now_r - prev_r == 1 and now_c - prev_c == -1:
        flag = False
    return flag


def back_tracking(col):
    global row, answer
    # print(col)
    if row == N:
        answer += 1
        print()
        return

    else:
        for n in range(N):
            if visited[n] == 0 and check(row, n, row-1, col):
                visited[n] = 1
                print(row, n, row-1, col)
                row += 1
                back_tracking(n)
                print('back')
                visited[n] = 0
                row -= 1


for i in range(N):
    visited[i] = 1
    row += 1
    back_tracking(i)

print(answer)