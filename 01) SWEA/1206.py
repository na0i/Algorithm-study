import sys
sys.stdin = open('1206.txt', 'r')

for tc in range(10):
    building_cnt = int(input())
    buildings = list(map(int, input().split()))

    nice_view = 0

    for b in range(2, len(buildings)-2):
        highest_b = max(buildings[b-2], buildings[b-1], buildings[b+1], buildings[b+2])

        if buildings[b] > highest_b:
            nice_view += buildings[b] - highest_b

    print('#{} {}'.format(tc+1, nice_view))
