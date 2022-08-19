N = int(input())
N_list = list(map(int, input().split()))
set_and_sorted_N_list = sorted(list(set(N_list)))

for i in range(len(set_and_sorted_N_list)):
    print(set_and_sorted_N_list[i], end=' ')