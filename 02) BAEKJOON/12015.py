import sys
import math
X, Y = map(int, sys.stdin.readline().rstrip().split())
Z = math.floor((Y * 100) / X)

start = 0
end = 1000000000

while start <= end:
    mid = (start + end) // 2

    new_x = X + mid
    new_y = Y + mid
    new_z = math.floor((new_y * 100) / new_x)

    if new_z > Z:
        end = mid - 1

    else:
        start = mid + 1

if Z >= 99:
    print(-1)

else:
    print(end + 1)