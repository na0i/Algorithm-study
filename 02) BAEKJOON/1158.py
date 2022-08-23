N, K = map(int, input().split())
circle_table = [_ for _ in range(1, N+1)]
result = []
index = 0


def get_index(k, list):
    global index
    index += k - 1

    if index >= len(list):
        index %= len(list)

    elif index < 0:
        index += len(list)

    return index


while circle_table:
    popped_idx = get_index(K, circle_table)
    popped = circle_table.pop(popped_idx)
    result.append(popped)


print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>')
