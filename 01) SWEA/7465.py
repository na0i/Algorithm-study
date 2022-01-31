import sys
sys.stdin = open('7465.txt', 'r')


def moori(now):
    global cnt
    for next in range(1, N+1):
        if people[now][next] == 1 and next not in visited:
            people[now][next] = 0
            visited.append(next)
            moori(next)

    flag = False
    for j in range(1, N+1):
        if people[now][j] == 1:
            flag = True

    if not flag:
        visited.append((0, now))


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    people = [[0] * (N+1) for _ in range(N+1)]
    visited = []
    x = []

    for _ in range(M):
        a, b = map(int, input().split())
        people[a][b] = 1
    cnt = 0
    for i in range(1, N+1):
        moori(i)

    print(visited)
    print(people)
    print(cnt)