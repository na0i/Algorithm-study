import sys
sys.stdin = open('6485.txt', 'r')

T = int(input())

for tc in range(T):
    bus_stop = [0] * 5001

    N = int(input())
    for n in range(N):
        A, B = list(map(int, input().split()))
        for i in range(A, B+1):
            bus_stop[i] += 1

    print('#{}'.format(tc+1), end=' ')

    P = int(input())
    for p in range(P):
        C = int(input())
        print(bus_stop[C], end=' ')
    print()