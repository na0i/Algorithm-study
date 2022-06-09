import sys
sys.stdin = open('5248.txt', 'r')


def make_team(curr_node):
    for next_node in range(1, N+1):
        if adj_list[curr_node][next_node] == 1 and visited[next_node] == 0:
            visited[next_node] = 1
            make_team(next_node)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    adj_list = [[0] * (N+1) for _ in range(N+1)]
    application = list(map(int, input().split()))
    visited = [0] * (N+1)

    for m in range(0, 2*M, 2):
        adj_list[application[m]][application[m+1]] = adj_list[application[m+1]][application[m]] = 1

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            make_team(i)

    print('#{} {}'.format(tc+1, cnt))