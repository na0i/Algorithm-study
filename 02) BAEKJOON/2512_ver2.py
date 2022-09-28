N = int(input())
request = list(map(int, input().split()))
budget = int(input())
request.sort()

start = 1
end = request[-1]

while start <= end:
    temp = 0
    mid = (start + end) // 2
    for cost in request:
        if cost <= mid:
            temp += cost
        else:
            temp += mid

    if temp > budget:
        end = mid - 1
    elif temp <= budget:
        start = mid + 1

print(end)