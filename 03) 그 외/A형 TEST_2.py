import sys
sys.stdin = open('A형 TEST_2.txt', 'r')


def psb_a(nodes):
    for i in range(N-6):
        nodes.append(i)
    return nodes


def psb_b(nodes):


T = int(input())
for tc in range(T):
    N = int(input())
    subway = list(map(int, input().split()))
    a = []
    b = []

    # print(psb_a(a))
    psb_a(a)
    