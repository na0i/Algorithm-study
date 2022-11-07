# intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# intervals = [[1,2],[1,2],[1,2]]
# intervals = [[1,2],[2,3]]
# intervals = [[1,6], [7,8], [7,9], [9,10]]
# intervals = [[1, 100], [1, 11], [2,11], [11,22]]
# intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
intervals = sorted(intervals, key=lambda x : x[0])
print(len(intervals),intervals)
cnt = 0

start = intervals[0][0]
end = intervals[0][1]

for i in range(len(intervals) - 1):
    next_start = intervals[i+1][0]
    next_end = intervals[i+1][1]
    print(start, end, '.',abs(end-start), '//', next_start, next_end, '.', abs(next_end-next_start), '//', cnt)

    if end > next_start:
        cnt += 1

        if abs(end - start) > abs(next_end - next_start):
            start = next_start
            end = next_end

    else:
        start = intervals[i+1][0]
        end = intervals[i+1][1]


print(cnt)

# max_interval = max(map(max, intervals))
#
# check = [0] * max_interval
# for inteval in sorted_intervals:
#     start = inteval[0]
#     end = inteval[1]
#
#     for i in range(start, end):
#         check[i] += 1
#
#
# cnt = 0
# for inteval in sorted_intervals:
#     start = inteval[0]
#     end = inteval[1]
#     flag = False
#
#     for j in range(start, end):
#         if check[j] > 1:
#             flag = True
#             break
#
#     if flag:
#         cnt += 1
#         for k in range(start, end):
#             check[k] -= 1
#
#     else:
#         continue
#
# print(cnt)
#
