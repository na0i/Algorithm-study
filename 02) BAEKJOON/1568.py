import sys
N = int(sys.stdin.readline())
birds = N
idx = 1
cnt = 0
while birds:
    cnt += 1

    if idx > birds:
        idx = 1
    for i in range(1, idx+1):
        birds -= 1

    idx += 1

print(cnt)