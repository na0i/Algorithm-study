import sys
sys.stdin = open('1232.txt', 'r')

for tc in range(10):
    N = int(input())
    tree = [0] * (N+1)
    for n in range(N):
        node_info = list(input().split())
        if node_info[1] == '+' or node_info[1] == '-' or node_info[1] == '/' or node_info[1] == '*':
            tree[int(node_info[0])] = node_info[1]
            left_ch = node_info[2]
            right_ch = node_info[3]
        else:
            tree[int(node_info[0])] = int(node_info[1])

    print(tree)