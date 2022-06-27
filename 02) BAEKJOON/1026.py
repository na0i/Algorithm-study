N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
sorted_A_list = sorted(A_list)
sorted_B_list = sorted(B_list)
sorted_B_list.reverse()

S = 0
for i in range(N):
    S += sorted_A_list[i] * sorted_B_list[i]

print(S)