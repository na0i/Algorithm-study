import sys
sys.stdin = open('5189.txt', 'r')


def DFS(curr, psb_battery):
    global now, final_battery
    if psb_battery > final_battery:
        return

    if 0 not in visited:
        now = curr
        final_battery = psb_battery
        return (now, final_battery)

    for i in range(N):
        next = i
        if visited[next] == 1 or curr == next: # 이미 방문했거나, 방문할 곳이 현재와 같은 경우
            continue
        if next == 0 and 0 in visited[1:]: # 전부 다 방문한 게 아닌데 next가 0이 되는 경우는 X
            continue
        else:
            visited[next] = 1
            DFS(next, psb_battery+golf_zone[curr][next])
            visited[next] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    golf_zone = [list(map(int, input().split())) for _ in range(N)]
    now = 0
    final_battery = 987654321
    visited = [0] * N

    DFS(0, 0)
    print('#{} {}'.format(tc+1, final_battery+golf_zone[now][0]))