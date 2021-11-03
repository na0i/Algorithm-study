# N, K = map(int, input().split())
# coin = [int(input()) for n in range(N)]
# coin = sorted(coin)
#
# cnt = 0
# for i in range(N-1, -1, -1):
#     cnt += K // coin[i]
#     K %= coin[i]
#
# print(cnt)


N, K = map(int, input().split())
coin = [int(input()) for n in range(N)]
coin = sorted(coin)

cnt = 0
current = 0
for i in range(N-1, -1, -1):
    if coin[i] > K:
        continue

    while current + coin[i] <= K:
        current += coin[i]
        cnt += 1

        if current >= K:
            break

print(cnt)