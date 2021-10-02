import sys
sys.stdin = open('4408.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    # room = list([[0] for i in range(201)] for j in range(2))
    room = [0] * 401

    for _ in range(N):
        current, togo = map(int, input().split())

        if current >= 2 and current % 2 == 0:
            current -= 1

        if togo >= 3 and togo % 2 == 1:
            togo += 1

        for i in range(current, togo+1):
            room[i] += 1

    count = 0
    overlapped = max(room)
    while overlapped > 0:
        for i in range(401):

            room_num = []
            if room[i] == overlapped:
                room_num.append(i)

        count += 1
        for j in range(len(room_num)):
            room[j] -= 1
        overlapped -= 1

    print('#{} {}'.format(tc+1, count))
