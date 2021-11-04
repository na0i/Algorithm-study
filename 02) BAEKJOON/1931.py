N = int(input())
conference = [tuple(map(int, input().split())) for _ in range(N)]
time = [0] * 987654321
using_time = []

for i in range(N):
    using_time.append((conference[i][1]-conference[i][0], conference[i]))

using_time = sorted(using_time)

cnt = 0
for j in range(N):
    flag = True
    start = using_time[j][1][0]
    end = using_time[j][1][1]

    if start != end:
        for k in range(start, end):
            if time[k] != 0:
                flag = False

        if flag == True:
            cnt += 1
            for l in range(start, end):
                time[l] += 1
    else:
        continue

print(cnt)