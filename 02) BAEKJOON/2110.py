import sys
N, C = map(int, sys.stdin.readline().rstrip().split())
x_coordinates = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
x_coordinates = sorted(x_coordinates)

start = x_coordinates[0]
end = x_coordinates[-1]

print(x_coordinates)
current_x = start
# while start <= end:
    # cnt = 1
    # mid = (start + end) // 2

