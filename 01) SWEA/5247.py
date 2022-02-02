import sys
sys.stdin = open('5247.txt', 'r')


def short_calcul(now, turn):
    global result
    if turn > result:
        return

    if now > limit:
        return

    if now == M:
        result = turn
        return


    for i in range(4):
        if i == 2:
            next = now * calcul[i]
            visited.append(next)
            short_calcul(next, turn+1)

        else:
            next = now + calcul[i]
            visited.append(next)
            short_calcul(next, turn+1)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    limit = 1000000
    result = 1000000
    calcul = [1, -1, 2, -10]
    visited = []

    short_calcul(N, 0)
    print(tc+1, result)
