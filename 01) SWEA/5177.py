import sys
sys.stdin = open('5177.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    tree = [0 for _ in range(N+1)]
    insert = 0

    for n in range(1, N+1):
        tree[n] = N_list[insert]
        insert += 1

        # now: 현재 idx
        # compare: 비교할 idx(부모 idx)
        now = n
        compare = now // 2

        while compare > 0 and tree[now] < tree[compare]:
            tree[now], tree[compare] = tree[compare], tree[now]
            now //= 2   # now도 계속 //2 하면서 올라가야함
            compare //= 2

    sum_idx = N
    answer = 0
    while sum_idx > 0:
        sum_idx //= 2
        answer += tree[sum_idx]

    print('#{} {}'.format(tc+1, answer))