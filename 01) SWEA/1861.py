import sys
sys.stdin = open('1861.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for curr_r in range(N):
        for curr_c in range(N):
            for d in range(4):
                next_r = curr_r + dr[d]
                next_c = curr_c + dc[d]

                if 0 <= next_r < N and 0 <= next_c < N and rooms[curr_r][curr_c] + 1 == rooms[next_r][next_c]:
                    visited[rooms[next_r][next_c]] = rooms[curr_r][curr_c]
    room_name = ''
    max_cnt = 1
    cnt = 1

    for i in range(len(visited)-1, 0, -1):
        if visited[i] != 0:
            cnt += 1

        if visited[i] == 0:
            if cnt >= max_cnt:
                max_cnt = cnt
                room_name = i
            cnt = 1

    print('#{} {} {}'.format(tc+1, room_name, max_cnt))