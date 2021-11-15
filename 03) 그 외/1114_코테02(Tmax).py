maps = list(list(map(int, input().split())) for _ in range(7))
p = int(input())
r = int(input())
N = 7

if r % 2 == 0:
    left_kill = 0
    for i in range(N):
        for j in range(N):
            monster = 0
            up_check = 0

            while up_check < r // 2 and 0 <= i < N and 0 <= j < N:
                for k in range(j+up_check, j+r-up_check):
                    if k < 0 or k >= N:
                        pass
                    elif k == j+up_check or k == j+r-up_check:
                        print(i, k, maps[i][k], '절반UP')

                        if maps[i][k] <= p//2:
                            monster += 1
                    else:
                        if maps[i][k] <= p:
                            monster += 1
                            print(i, k, maps[i][k], '저기')
                up_check += 1
                i -= 1
                j += 1

            down_check = 0
            while down_check < r // 2 and 0 <= i < N and 0 <= j < N:
                for k in range(j+down_check, j+r-down_check):
                    if k < 0 or k >= N:
                        pass
                    elif k == j+down_check or k == j+r-down_check:
                        print(i, k, maps[i + 1][k], '절반')

                        if maps[i+1][k] <= p//2:
                            monster += 1

                    else:
                        if maps[i+1][k] <= p:
                            monster += 1
                            print(i, k, maps[i+1][k], ' 시발')

                down_check += 1
                i += 1
                j += 1

            print(monster)
            print()
            if left_kill <= monster:
                left_kill = monster

    right_kill = 0

    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            monster = 0
            up_check = 0

            while up_check < r // 2 and 0 <= i < N and 0 <= j < N:
                for k in range(j - r + up_check+1, j-up_check+1):
                    if k < 0 or k >= N:
                        pass
                    elif k == j -r +up_check +1 or k == j - up_check+1:
                        print(i, k, maps[i][k], '절반UP')

                        if maps[i][k] <= p // 2:
                            monster += 1
                    else:
                        if maps[i][k] <= p:
                            monster += 1
                            print(i, k, maps[i][k], '저기')
                up_check += 1
                i -= 1
                j += 1

            down_check = 0
            while down_check < r // 2 and 0 <= i < N and 0 <= j < N:
                for k in range(j - r + down_check+1, j-down_check+1):
                    if k < 0 or k >= N:
                        pass
                    elif k == j-r+down_check+1 or k == j - down_check + 1:
                        print(i, k, maps[i + 1][k], '절반')

                        if maps[i + 1][k] <= p // 2:
                            monster += 1

                    else:
                        if maps[i + 1][k] <= p:
                            monster += 1
                            print(i, k, maps[i][k], ' 시발')

                down_check += 1
                i += 1
                j -= 1

            if right_kill <= monster:
                right_kill = monster

    print()
    print(left_kill, right_kill)
