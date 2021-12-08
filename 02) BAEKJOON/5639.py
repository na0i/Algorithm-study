nodes = []
while True:
    node = input()
    if not node:
        break
    nodes.append(int(node))

size = len(nodes)
tree = [0] * size

for n in range(size):
    tree[n] = nodes[n]

