import sys
N = int(input())
N_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(input())
M_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 이분 탐색 문제이지만
# 단일 타겟을 찾지 않기 때문에 시간초과가 발생

dict = {}

for i in N_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

result = []
for j in M_list:
    if j in dict:
        result.append(dict[j])
    else:
        result.append(0)

for k in result:
    print(k, end=' ')