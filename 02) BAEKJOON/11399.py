N = int(input())
P_list = list(map(int, input().split()))
sorted_P_list = sorted(P_list)

temp_sum = []
for i in range(N):
    temp_sum.append(sum(sorted_P_list[:i+1]))

print(sum(temp_sum))