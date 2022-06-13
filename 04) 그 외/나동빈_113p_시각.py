import sys
sys.stdin = open('나동빈_113p_시각.txt', 'r')

N = int(input())
cnt = 0
for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            hour_min_and_sec = str(hour) + str(minute) + str(second)
            if '3' in hour_min_and_sec:
                cnt += 1

print(cnt)