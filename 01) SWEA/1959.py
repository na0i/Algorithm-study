import sys
sys.stdin = open('1959.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = []

    if N <= M:
        idx = 0
        while idx <= M-N:
            summ = 0
            for n in range(N):
                summ += A[n] * B[idx+n]
            idx += 1
            result.append(summ)

    else:
        idx = 0
        while idx <= N-M:
            summ = 0
            for m in range(M):
                summ += A[idx+m] * B[m]
            idx += 1
            result.append(summ)

    print('#{} {}'.format(tc+1, max(result)))

