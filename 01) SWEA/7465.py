import sys
sys.stdin = open('7465.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nodes = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        nodes[a][b] = nodes[b][a] = 1

    cnt = 0
    for node in range(1, N+1):
        if visited[node] == 0:
            visited[node] = 1
            stack = [node]
            cnt += 1

            while stack:
                now = stack.pop(0)
                for i in range(1, N+1):
                    if visited[i] == 0 and nodes[now][i] == 1:
                        visited[i] = 1
                        stack.append(i)

    print('#{} {}'.format(tc+1, cnt))