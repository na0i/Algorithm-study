import sys
sys.stdin = open('4843.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))

    ori = sorted(N_list)
    result = []

    for i in range(N//2):
        result.append(ori[N-i-1])
        result.append(ori[i])

        if len(result) == 10:
            break

    print('#{}'.format(tc+1), end=' ')
    for j in range(10):
        print(result[j], end=' ')
    print()