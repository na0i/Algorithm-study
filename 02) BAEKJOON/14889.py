import itertools
from itertools import combinations

N = int(input())
N_list = []
for _ in range(N):  # 조합 만들기 위한 임시 배열 [0, 1, 2, 3]
    N_list.append(_)
S_list = [list(map(int, input().split())) for _ in range(N)]
team_combinations = list(combinations(N_list, N // 2))
cnt_combinations = len(team_combinations)
start_team_combinations = team_combinations[:cnt_combinations//2]  # 조합 결과 중 앞 절반
link_team_combinations = team_combinations[cnt_combinations//2:]  # 조합 결과 중 뒤 절반

min_gap = 987654321
for i in range(cnt_combinations // 2):
    start_score = 0
    link_score = 0

    start_team = start_team_combinations[i]
    link_team = link_team_combinations[len(link_team_combinations) - i - 1]

    for j in start_team:  # start_team 예시: (0, 1, 2)
        for k in start_team:
            if k != j:  # (0, 0), (1, 1), (2, 2) 방지
                start_score += S_list[j][k]

    for j in link_team:   # link_team 예시: (3, 4, 5)
        for k in link_team:
            if k != j:
                link_score += S_list[j][k]

    min_gap = min(abs(start_score - link_score), min_gap)

print(min_gap)

# team_combinations: [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# start_team_combinations: [(0, 1), (0, 2), (0, 3)]
# link_team_combinations: [(1, 2), (1, 3), (2, 3)]
# start_team_combinations[0]번째와 link_team_combinations[-1]번째가 같은 경기에 출전
