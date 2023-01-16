cnt = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

price_idx_dict = {}
for i in range(len(price)):
    price_idx_dict[i] = price[i]

price_idx = sorted(price_idx_dict, key=lambda x:price_idx_dict[x])
end = len(price) - 1

answer = 0
for start in price_idx:
    if start >= end:
        continue

    else:
        answer += sum(distance[start:end]) * price[start]
        end = start

print(answer)

# 이렇게 복잡하게 풀 게 아니었는데..
# 좋은 코드 예시!
# N = int(input())
# road = [int(x) for x in input().split()]
# price = [int(x) for x in input().split()]
# cost = price[0]
# final = 0
# for i in range(N - 1):
#     if price[i] < cost:
#         cost = price[i]
#     final += road[i] * cost
# print(final)
