import sys
sys.stdin = open('5174.txt', 'r')


def child_cnt(s):
    global cnt

    if left[s] != 0:
        cnt += 1
        child_cnt(left[s])

    if right[s] != 0:
        cnt += 1
        child_cnt(right[s])

    if left[s] == 0 and right[s] == 0:
        return

    return cnt


T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    pair = list(map(int, input().split()))
    cnt = 1

    left = [0 for _ in range(E+2)]
    right = [0 for _ in range(E+2)]

    for i in range(0, 2*E, 2):
        if left[pair[i]] == 0:
            left[pair[i]] = pair[i+1]

        else:
            right[pair[i]] = pair[i+1]

    child_cnt(N)
    print('#{} {}'.format(tc+1, cnt))