import sys
sys.stdin = open('나동빈_92p_큰 수의 법칙.txt', 'r')

N, M, K = map(int, input().split())
number_list = list(map(int, input().split()))
sorted_number_list = sorted(number_list)

answer = 0
cnt = 0
while cnt < M:
    idx_cnt = 0

    while idx_cnt < K:
        idx_cnt += 1
        answer += sorted_number_list[-1]

    cnt += idx_cnt
    if cnt < M:
        answer += sorted_number_list[-2]
        cnt += 1

print(answer)