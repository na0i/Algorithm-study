from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_list = list(combinations(cards, 3))

answer = 0
for i in range(len(cards_list)):
    cards_sum = sum(cards_list[i])
    if cards_sum > M:
        continue

    elif cards_sum < M:
        if cards_sum > answer:
            answer = cards_sum

    elif cards_sum == M:
        answer = cards_sum

print(answer)