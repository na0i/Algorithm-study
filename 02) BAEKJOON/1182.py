from itertools import combinations

N, S = map(int, input().split())
N_list = list(map(int, input().split()))
answer = 0

for cnt in range(1, N+1):
    cnt_combinations = combinations(N_list, cnt)
    for comb in cnt_combinations:
        if sum(comb) == S:
            answer += 1

print(answer)