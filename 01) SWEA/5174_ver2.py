import sys
sys.stdin = open('5174.txt', 'r')


def find_child(now):
    global cnt
    cnt += 1

    if left[now] != 0:
        if right[now] != 0:
            find_child(right[now])
        find_child(left[now])

    return cnt

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    pair = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)
    for p in range(0, 2*E, 2):
        if left[pair[p]] != 0:
            right[pair[p]] = pair[p+1]
        else:
            left[pair[p]] = pair[p+1]

    cnt = 0
    find_child(N)
    print('#{} {}'.format(tc+1, cnt))