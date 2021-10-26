N = int(input())
dunchi = [list(map(int, input().split())) for _ in range(N)]
cnts = []

for i in range(N):
    cnt = N - 1
    for j in range(N):
        if dunchi[i][0] < dunchi[j][0] and dunchi[i][1] < dunchi[j][1]:
            cnt -= 1
    cnts.append(cnt)

answer = ''
for k in range(N):
    answer += str(N - cnts[k]) + ' '

print(answer)