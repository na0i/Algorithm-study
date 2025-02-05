n = 6
times = [7, 10]
min_time = min(times)
max_time = max(times) * n
answer = 0
while min_time <= max_time:
    mid = (min_time + max_time) // 2

    people = 0
    for time in times:
        people += mid // time

    if people >= n:
        result = mid
        max_time = mid - 1

    else:
        min_time = mid + 1

