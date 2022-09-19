N, K = map(int, input().split())
dolls = list(map(int, input().split()))

start = 0
end = 0
ryan_cnt = 0
result = 987654321


def check_cnt(check_list):
    check_list = sorted(check_list)
    cnt = 0

    for i in range(len(check_list)):
        if check_list[i] == 1:
            cnt += 1
        else:
            break

    return cnt


while start <= end < N:
    if check_cnt(dolls[start:end+1]) < K:
        end += 1
    elif check_cnt(dolls[start:end+1]) == K:
        result = min(result, end - start) + 1
        start += 1

if result == 987654321:
    print(-1)
else:
    print(result)