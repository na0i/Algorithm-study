import sys
sys.stdin = open('5789.txt', 'r')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for q in range(Q):
        L, R = map(int, input().split())

        for i in range(L-1, R):
            boxes[i] = q + 1

    result = ''
    for n in range(N):
        result += str(boxes[n]) + ' '

    print('#{} {}'.format(tc+1, result))