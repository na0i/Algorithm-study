K, N = map(int, input().split())
lan_cables = [int(input()) for _ in range(K)]
lan_cables = sorted(lan_cables)

min_len = 1
max_len = max(lan_cables)

while min_len <= max_len:
    mid = (min_len + max_len) // 2

    cnt = 0
    for cable in lan_cables:
        cnt += cable // mid

    if cnt < N:
        max_len = mid - 1

    else:
        min_len = mid + 1


print(max_len)
