N, K = map(int, input().split())
table = [i for i in range(1, N+1)]
result = []
idx = K - 1

if len(table) == 1:
    result.append(str(table[0]))

else:
    while table and len(result) != N:
        result.append(str(table.pop(idx)))
        idx += K - 1

        while idx >= len(table):
            idx -= len(table)
            if len(table) == 0:
                break

print('<', end='')
print(', '.join(result), end='')
print('>')