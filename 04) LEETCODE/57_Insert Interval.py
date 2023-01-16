intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

intervals.append(newInterval)
new_intervals = sorted(intervals)

result = [new_intervals[0]]

for idx in range(1, len(new_intervals)):
    now = result[-1]
    next = new_intervals[idx]

    if now[1] < next[0]:
        result.append(next)

    else:
        start = now[0]
        end = max(now[1], next[1])

        result[-1] = [start, end]

print(result)