root = [3, 9, 20, None, None, 15, 7, 6, None, None, None]
child = deque(copy.deepcopy(root)[1:])
result = []
if root:
    result.append([root[0]])
    for rootNode in root:
        while child:
            left_child = child.popleft()
            right_child = child.popleft()

            if not left_child and right_child:
                temp = [right_child]

            elif left_child and not right_child:
                temp = [left_child]

            elif not left_child and not right_child:
                continue

            else:
                temp = [left_child, right_child]

            result.append(temp)


print(result)