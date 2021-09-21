import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))

    N_list = [list(map(int, input().split())) for _ in range(N)]

    total_killed = []

    for i in range(N-M+1):
        for j in range(N-M+1):

            pari = 0
            for k in range(M):
                for l in range(M):
                    pari += N_list[i+k][j+l]

            total_killed.append(pari)

    print('#{} {}'.format(tc+1, max(total_killed)))