nodes = []
while True:
    node = input()
    if not node:
        break
    nodes.append(int(node))

root = nodes[0]
size = len(nodes)


def binary_search():