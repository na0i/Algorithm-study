import sys
sys.stdin = open('1218.txt', 'r')

for tc in range(10):
    length = int(input())
    gwalho = list(input())

    pair = {'(': -1, ')': 1, '[': -2, ']': 2, '{': -3, '}':3, '<': -4, '>':4 }

    stack = []
    for i in range(length):
        stack.append(gwalho[i])

        while len(stack) >= 2 and pair[stack[-1]] + pair[stack[-2]] == 0:
            stack.pop()
            stack.pop()

    if len(stack) == 0:
        print('#{} {}'.format(tc+1, 1))
    else:
        print('#{} {}'.format(tc+1, 0))
