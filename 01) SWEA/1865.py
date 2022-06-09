import sys
sys.stdin = open('1865.txt', 'r')


def dfs(essence, turn):
    global result
    # 이부분 없으면 제한시간 초과
    if essence == 0:
        return

    if essence < result:
        return

    if turn == N:
        result = essence
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(essence*percantage[turn][i]/100, turn+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -987654321
    visited = [0] * N
    percantage = []
    for _ in range(N):
         percantage.append(list(map(int, input().split())))

    dfs(1, 0)

    print('#{} {:.6f}'.format(tc, result*100))