N = int(input())
tree = {}


def jeonwui(now):
    global result_j
    if now != '.':
        print(now, end='')
        jeonwui(tree[now][0])
        jeonwui(tree[now][1])


def zoongwui(now):
    if now != '.':
        zoongwui(tree[now][0])
        print(now, end='')
        zoongwui(tree[now][1])


def hoowui(now):
    if now != '.':
        hoowui(tree[now][0])
        hoowui(tree[now][1])
        print(now, end='')


for n in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

jeonwui('A')
print()
zoongwui('A')
print()
hoowui('A')

