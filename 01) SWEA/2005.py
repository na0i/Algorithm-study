import sys
sys.stdin = open('2005.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())


    answer = [[] for _ in range(N)]

    for i in range(N):

        if i == 0:
            answer[i] = [1]

        elif i == 1:
            answer[i] = [1, 1]

        else:
            answer[i].append(1)

            idx = 1
            while idx < i:
                answer[i].append(answer[i-1][idx-1] + answer[i-1][idx])
                idx += 1

            answer[i].append(1)

    print('#{}'.format(tc+1))

    for i in range(N):
        for j in range(i+1):
            print(answer[i][j], end=' ')
        print()