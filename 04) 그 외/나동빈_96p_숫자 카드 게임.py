import sys
sys.stdin = open('나동빈_96p_숫자 카드 게임.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]

    min_cards = []
    for i in range(N):
        min_cards.append(min(cards[i]))

    print(max(min_cards))