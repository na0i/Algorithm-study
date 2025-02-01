n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
visited = [0 for _ in range(n)]
nodes_computers = []

for i in range(n):
    i_stack = []
    for j in range(n):
        if i == j:
            continue
        elif computers[i][j] == 1:
            i_stack.append(j)

    nodes_computers.append(i_stack)


result = 0
for node_idx in range(n):
    if visited[node_idx]:
        continue
    elif len(nodes_computers[node_idx]) == 0:
        result += 1
        continue
    else:
        result += 1
        stack = [node_idx]
        while stack:
            now = stack.pop()
            visited[now] = 1

            for next_node in nodes_computers[now]:
                if not visited[next_node]:
                    stack.append(next_node)

print(result)