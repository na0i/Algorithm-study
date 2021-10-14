import sys
sys.stdin = open('4873.txt', 'r')

T = int(input())
for tc in range(T):
    strr = list(input())

    stack = []
    for i in range(len(strr)):
        now = strr[i]
        if stack:
            if now == stack[-1]:
                stack.pop()
            else:
                stack.append(now)
        else:
            stack.append(now)

    print('#{} {}'.format(tc+1, len(stack)))