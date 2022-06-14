import sys
sys.stdin = open('나동빈_149p_음료수 얼려먹기.txt', 'r')


def dfs(graph, current_r, current_c):
    graph[current_r][current_c] = '1'
    for d in range(4):
        next_r = current_r + dr[d]
        next_c = current_c + dc[d]
        if 0 <= next_r < N and 0 <= next_c < M and graph[next_r][next_c] == '0':
            dfs(graph, next_r, next_c)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [list(map(str, input())) for _ in range(N)]
    ice_cnt = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if board[i][j] == '0':
                ice_cnt += 1
                dfs(board, i, j)
    
    print(ice_cnt)