import sys
sys.stdin = open('1210.txt', 'r')

for t in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    y = 99

    while y > 0:
        y -= 1
        
        # if와 while 문 모두에 x 범위 조건 걸기
        if 0 <= x-1 <= 99 and ladder[y][x-1] == 1:
            while 0 <= x-1 <= 99 and ladder[y][x-1] == 1:
                x -= 1

        elif 0 <= x+1 <= 99 and ladder[y][x+1] == 1:
            while 0 <= x+1 <= 99 and ladder[y][x+1] == 1:
                x += 1

    print('#{} {}'.format(tc, x))