import sys
sys.stdin = open('5201.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    freight = list(reversed(sorted(list(map(int, input().split())))))
    truck = list(reversed(sorted(list(map(int, input().split())))))

    answer = 0
    # print(freight, truck)
    while truck and freight:
        if freight[0] <= truck[0]:
            answer += freight[0]
            freight.pop(0)
            truck.pop(0)
        else:
            freight.pop(0)

    print('#{} {}'.format(tc+1, answer))