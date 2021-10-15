import sys
sys.stdin = open('4834.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(input())

    check = [0] * 10

    for i in range(N):
        idx = int(cards[i])
        check[idx] += 1

    num = 0
    often = 0
    for j in range(10):
        if check[j] >= often:
            often = check[j]
            num = j

    print('#{} {} {}'.format(tc+1, num, often))