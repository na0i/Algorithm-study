from bisect import bisect_left, bisect_right

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

result = []
for num in M_list:
    result.append(bisect_right(N_list, num) - bisect_left(N_list, num))

for r in result:
    print(r, end=" ")
