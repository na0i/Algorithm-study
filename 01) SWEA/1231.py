import sys
sys.stdin = open('1231.txt', 'r')


def zoongwui(now):
    global result
    if now:
        zoongwui(left[now])
        result += tree[now]
        zoongwui(right[now])

    return result


for tc in range(10):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = ''

    for n in range(N):
        node_info = list(map(str, input().split()))

        node_num = int(node_info[0])
        node_strr = node_info[1]

        if len(node_info) == 3:
            left_child = int(node_info[2])
            left[node_num] = left_child

        elif len(node_info) == 4:
            left_child = int(node_info[2])
            right_child = int(node_info[3])
            left[node_num] = left_child
            right[node_num] = right_child

        tree[node_num] = node_strr

    print('#{} {}'.format(tc+1, zoongwui(1)))