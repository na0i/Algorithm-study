N = int(input())
N_list = []

for i in range(N):
    x, y = map(int, input().split())
    N_list.append([y, x])

N_list = sorted(N_list)

for j in range(N):
    print(N_list[j][1], N_list[j][0])