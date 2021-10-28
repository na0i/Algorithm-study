T = int(input())
for tc in range(T):
    gwalho = input()

    stack = []
    for i in range(len(gwalho)):
        if stack:
            if gwalho[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(gwalho[i])
        else:
            stack.append(gwalho[i])

    if stack:
        print('NO')
    else:
        print('YES')