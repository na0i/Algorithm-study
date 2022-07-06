import sys
N = int(input())
N_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(input())
M_list = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
for i in range(M):
    flag = False
    start = 0
    end = N - 1
    now_card = M_list[i]
    while start <= end:
        mid = (start + end) // 2

        if now_card == N_list[mid]:
            flag = True
            cnt = 0
            for j in range(start, end+1):
                if N_list[j] < now_card:
                    continue
                elif N_list[j] > now_card:
                    break
                elif N_list[j] == now_card:
                    cnt += 1
            result.append(cnt)
            break

        elif now_card > N_list[mid]:
            start = mid + 1

        elif now_card < N_list[mid]:
            end = mid - 1

    if flag is False:
        result.append(0)

for i in range(len(result)):
    print(result[i], end=' ')