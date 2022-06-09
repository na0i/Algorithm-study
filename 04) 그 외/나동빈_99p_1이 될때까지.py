import sys
sys.stdin = open('나동빈_99p_1이 될때까지.txt', 'r')

N, K = map(int, input().split())

cnt = 0
while N > 1:
    if N == 1:
        break
    elif N >= K and N % K == 0:
        N //= K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)