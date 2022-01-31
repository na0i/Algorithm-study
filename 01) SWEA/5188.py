import sys
sys.stdin = open('5188.txt', 'r')


def dfs(curr_r, curr_c, psb_path):
    global final_path

    if psb_path > final_path:
        return

    if curr_r == N - 1 and curr_c == N - 1:
        final_path = psb_path
        return final_path

    for d in range(2):
        next_r = curr_r + dr[d]
        next_c = curr_c + dc[d]

        if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == 0:
            visited[next_r][next_c] = 1
            dfs(next_r, next_c, psb_path + board[next_r][next_c])
            visited[next_r][next_c] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    dr = [0, 1]
    dc = [1, 0]
    visited = [[0] * N for _ in range(N)]
    final_path = 987654321

    # board input
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    dfs(0, 0, board[0][0])

    print('#'+str(tc+1), final_path)