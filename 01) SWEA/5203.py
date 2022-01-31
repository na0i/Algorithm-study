import sys
sys.stdin = open('5203.txt', 'r')

T = int(input())
for tc in range(T):
    cards = list(map(int, input().split()))

    player_1 = []
    player_2 = []
    for card in range(0, 12, 2):
        player_1.append(cards[card])
        player_2.append(cards[card+1])

    result_1 = []
    result_2 = []
    answer = 0
    for turn in range(6):
        result_1.append(player_1.pop(0))
        result_2.append(player_2.pop(0))

        if turn >= 2:
            result_1 = sorted(result_1)
            result_2 = sorted(result_2)

            for i in range(len(result_1)-2):
                if result_1[i] == result_1[i+1] == result_1[i+2] or result_1[i] + 2 == result_1[i+1] + 1 == result_1[i+2]:
                    answer = 1
                    break
                elif result_2[i] == result_2[i+1] == result_2[i+2] or result_2[i] + 2 == result_2[i+1] + 1 == result_2[i+2]:
                    answer = 2
                    break

            if answer != 0:
                break

    print('#{} {}'.format(tc + 1, answer))