N = int(input())
left_tree = [0] * N
right_tree = [0] * N
result_1 = []
result_2 = []
result_3 = []
# [1, 3, 4, 0, 0, 0, 0]
# [2, 0, 5, 0, 6, 0, 0]

for n in range(N):
    node, left, right = map(str, input().split())
    if right == '.' and left == '.':
        pass
    elif left == '.' and right != '.':
        right_tree[n] = ord(right) - 65
    elif right == '.' and left != '.':
        left_tree[n] = ord(left) - 65
    else:
        left_tree[n] = ord(left) - 65
        right_tree[n] = ord(right) - 65


def jeonwui(now):
    global result_1

    result_1.append(now)

    if left_tree[now]:
        jeonwui(left_tree[now])

    if right_tree[now]:
        jeonwui(right_tree[now])

    return result_1


def zoongwui(now):
    global result_2

    if left_tree[now] or right_tree[now]:
        zoongwui(left_tree[now])
        result_2.append(now)
        zoongwui(right_tree[now])

    return result_2


def hoowui(now):
    global result_3

    if left_tree[now]:
        hoowui(left_tree[now])

    if right_tree[now]:
        hoowui(right_tree[now])
    result_3.append(now)

    return result_3

jeonwui(0)
zoongwui(0)
hoowui(0)


for i in range(len(result_1)):
    print(chr(result_1[i] + 65), end='')

print()
for j in range(len(result_2)):
    print(chr(result_2[j] + 65), end='')

print()
for k in range(len(result_3)):
    print(chr(result_3[k] + 65), end='')