N = int(input())
conference = [list(map(int, input().split())) for _ in range(N)]
conference = sorted(conference, key=lambda x: (x[1], x[0]))

can_meet = [conference[0]]
for i in range(1, N):
    if conference[i][0] >= can_meet[-1][1]:
        can_meet.append(conference[i])

    elif conference[i][0] == conference[i][1]:
        can_meet.append(conference[i])

print(len(can_meet))