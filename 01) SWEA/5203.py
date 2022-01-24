import sys
sys.stdin = open('5203.txt', 'r')

T = int(input())
for tc in range(T):
    cards = list(map(int, input().split()))
    player1 = sorted(cards[:6])
    player2 = sorted(cards[6:])

