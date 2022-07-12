import sys
N, C = map(int, sys.stdin.readline().rstrip().split())
x_coordinate = [int(input()) for _ in range(N)]
x_coordinate = sorted(x_coordinate)

start = x_coordinate[0]
end = x_coordinate[-1]

check = [0] * (end+1)
for x in x_coordinate:
    check[x] = 1
print(x_coordinate)
print(check)
while start <= end:
    mid = (start + end) // 2
    print(start, mid, end)
    cnt = 1
    next_x = start + mid
    while True:
        if next_x > end:
            break
        elif check[next_x] == 1:
            cnt += 1
        next_x += mid

    if cnt < C:
        start = mid + 1

    else:
        end = mid - 1
        if cnt == C:
            print(start, end, mid, 'd')

print(end)