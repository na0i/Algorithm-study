import sys
sys.stdin = open('1859.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    sell = price[N-1]
    profit = 0
    for i in range(N-1, -1, -1):
        if price[i] >= sell:
            sell = price[i]
        else:
            profit += sell - price[i]

    print('#{} {}'.format(tc+1, profit))