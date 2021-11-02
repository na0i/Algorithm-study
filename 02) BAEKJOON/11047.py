N, K = map(int, input().split())
coin = [int(input()) for n in range(N)]

for i in range(N-1, 0, -1):
    if coin[i] > K:
        continue

    current = 0
    if coin[i] <= K:
        while True:
            current += coin[i]
            cnt += 1