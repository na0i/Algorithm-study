N = int(input())
num_list = [int(input()) for _ in range(N)]
idx = 0
stack = []
answer = []
while num_list:
    now = num_list.pop(0)

    while idx < now:
        idx += 1
        stack.append(idx)
        answer.append('+')

    if idx == now:
        stack.pop()
        answer.append('-')
        while stack and num_list and stack[-1] == num_list[0]:
            stack.pop()
            answer.append('-')
            num_list.pop(0)

if stack:
    print('NO')

else:
    for i in range(len(answer)):
        print(answer[i])