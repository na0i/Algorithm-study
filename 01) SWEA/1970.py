import sys
sys.stdin = open('1970.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    for i in range(len(money)):
        cnt = N // money[i]

        if cnt != 0:
            N -= money[i] * cnt

        result.append(cnt)

    print('#{}'.format(tc+1))
    print(*result)