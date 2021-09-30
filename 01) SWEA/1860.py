import sys
sys.stdin = open('1860.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    fish = [0 for i in range(11112)]
    arrive = sorted(arrive)

    for i in range(M, 11112, M):
        fish[i] += K

    def is_possible():
        message = 'Possible'
        for j in range(N):
            if sum(fish[:arrive[j]+1]) - 1 < 0:
                message = 'Impossible'
                return message
            fish[0] -= 1
        return message

    print('#{} {}'.format(tc+1, is_possible()))
