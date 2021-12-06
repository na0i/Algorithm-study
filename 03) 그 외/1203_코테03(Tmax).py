n = 4
costs = [10, 10, 5, 6]
edges = [[3, 1, 2], [1, 2, 1], [4, 1, 2], [4, 2, 3]]
node_list_ori = [[0] * (n+1) for _ in range(n+1)]
node_list_rev = [[0] * (n+1) for _ in range(n+1)]
ingredient = 0
people = 0

def final_cost(now):
    global ingredient, people

    for l in range(1, n+1):
        how_many = node_list_rev[now][l]
        if how_many != 0:
            final_cost(l)

    return ingredient, people

for i in range(len(edges)):
    start = edges[i][0]
    end = edges[i][1]
    many = edges[i][2]

    node_list_ori[start][end] = 1
    node_list_rev[end][start] = many
    start = 0

    for j in range(1, n+1):
        flag = True
        for k in range(1, n+1):
            if node_list_ori[j][k] != 0:
                flag = False
                break
        if flag == True:
            start = j

print(node_list_ori)
print(node_list_rev)
print(final_cost(start))
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, (True, 3), 0],
# [0, 0, 0, 0, (True, 2), (True, 1), 0, 0, 0],
# [0, 0, 0, 0, (True, 1), (True, 2), 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, (True, 1), 0],
# [0, 0, 0, 0, 0, 0, 0, (True, 2), 0],
# [0, 0, 0, 0, 0, 0, 0, (True, 1), 0],
# [0, 0, 0, 0, 0, 0, 0, 0, (True, 2)],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 반대로
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 2, 1, 0, 0, 0, 0, 0],
# [0, 0, 1, 2, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 3, 0, 0, 1, 2, 1, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 2, 0]]