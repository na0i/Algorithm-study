import sys
sys.stdin = open('1234.txt', 'r')

for tc in range(10):
    test_case, strr = map(str, input().split())

    stack = []
    for i in range(len(strr)):
        if stack and stack[-1] == strr[i]:
            stack.pop()
        else:
            stack.append(strr[i])
    print('#{} {}'.format(tc+1, ''.join(stack)))
