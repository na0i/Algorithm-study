import sys
sys.stdin = open('2814.txt', 'r')


def find_logest(now):
    global far, temp
    # 최장거리이므로 이조건만 있으면 된다.
    if far > temp:
        temp = far
        return

    for k in range(N + 1):
        if nodes[now][k] == 1 and visited[k] == 0:
            far += 1
            visited[k] = 1
            find_logest(k)
            visited[k] = 0
            far -= 1


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nodes = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    # 연결된 정점 입력
    if N > 1:
        for _ in range(M):
            x, y = map(int, input().split())
            nodes[x][y] = 1
            nodes[y][x] = 1

        far = 0
        temp = -987654321

        for i in range(1, N+1):
            for j in range(1, N+1):
                if nodes[i][j] == 1:
                    find_logest(j)

        print('#{} {}'.format(tc+1, temp))

    else:
        print('#{} {}'.format(tc+1, 1))
