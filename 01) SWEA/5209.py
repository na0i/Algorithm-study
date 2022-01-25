import sys
sys.stdin = open('5209.txt', 'r')


def min_cost(curr, psb_cost):
    global final_cost

    if psb_cost > final_cost:
        return

    if curr == N:
        final_cost = psb_cost
        return final_cost

    if curr < N:
        for factory in range(N):
            if visited[factory] == 0:
                visited[factory] = 1
                psb_cost += costs[curr][factory]
                curr += 1
                min_cost(curr, psb_cost)
                curr -= 1
                visited[factory] = 0
                psb_cost -= costs[curr][factory]


T = int(input())
for tc in range(T):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    final_cost = 987654321

    min_cost(0, 0)
    print('#{} {}'.format(tc+1, final_cost))