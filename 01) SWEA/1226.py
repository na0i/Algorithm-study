import sys
sys.stdin = open('1226.txt', 'r')

for tc in range(10):
    test_case = int(input())
    miro = [list(map(int, input())) for _ in range(16)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[0] * 16 for _ in range(16)]

    start_r = 1
    start_c = 1

    stack = [(start_r, start_c)]
    flag = 0

    while stack:
        now = stack.pop()
        visited[now[0]][now[1]] = 1

        for d in range(4):
            next_r = now[0] + dr[d]
            next_c = now[1] + dc[d]
            if 0 <= next_r <= 15 and 0 <= next_c <= 15 and visited[next_r][next_c] != 1 and miro[next_r][next_c] == 0:
                stack.append((next_r, next_c))
                visited[next_r][next_c] = 1

            if next_r == 13 and next_c == 13:
                # if miro[next_r][next_c] == 3:
                flag = 1

    print('#{} {}'.format(tc+1, flag))