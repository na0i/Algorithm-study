import sys
sys.stdin = open('1217.txt', 'r')

for tc in range(10):
    test_case = int(input())
    N, M = map(int, input().split())


    cnt = 0
    result = 1

    def squared(n, m):
        global cnt
        global result

        result *= n
        cnt += 1

        while cnt < m:
            squared(n, m)

        return result

    print('#{} {}'.format(test_case, squared(N, M)))