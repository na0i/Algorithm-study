import sys
N = int(sys.stdin.readline().rstrip())
budget = list(map(int, sys.stdin.readline().rstrip().split()))
sum_budget = int(sys.stdin.readline().rstrip())
budget = sorted(budget)

start = 1
end = budget[-1]

while start <= end:
    mid = (start + end) // 2

    amount = 0
    for i in range(N):
        if budget[i] < mid:
            amount += budget[i]
        else:
            amount += mid

    if amount <= sum_budget:
        start = mid + 1

    else:
        end = mid - 1

print(end)