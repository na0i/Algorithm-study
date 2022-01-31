import sys
sys.stdin = open('5208.txt', 'r')


def backtracking(curr, psb_cnt):
    global min_cnt

    if psb_cnt > min_cnt:
        return

    if curr >= N-1:
        min_cnt = psb_cnt
        return min_cnt

    if curr < N-1:
        # for문 거꾸로 세어야함
        # 그렇지 않을 경우 제한시간 초과
        for i in range(curr+bus_stop[curr], curr, -1):
            backtracking(i, psb_cnt+1)


T = int(input())
for tc in range(T):
    battery = list(map(int, input().split()))
    N = battery[0]
    bus_stop = battery[1:]
    min_cnt = 987654321

    backtracking(0, 0)
    print('#{} {}'.format(tc+1, min_cnt-1))