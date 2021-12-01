import sys
sys.stdin = open('5178.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]

    for m in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    for i in range(N-M, 0, -1):
        idx = i
        if idx*2 <= N and idx*2+1 <= N:
            tree[idx] = tree[idx*2] + tree[idx*2+1]
        else:
            tree[idx] = tree[idx*2]

    print('#{} {}'.format(tc+1, tree[L]))