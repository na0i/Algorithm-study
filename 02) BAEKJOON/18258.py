from collections import deque
import sys

N = int(input())
myqueue = deque()

for n in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == 'pop':
        if len(myqueue) == 0:
            print(-1)
        else:
            x = myqueue.popleft()
            print(x)

    elif command[0] == 'size':
        print(len(myqueue))

    elif command[0] == 'empty':
        if len(myqueue) == 0:
            print(1)

        else:
            print(0)

    elif command[0] == 'front':
        if len(myqueue) == 0:
            print(-1)

        else:
            print(myqueue[0])

    elif command[0] == 'back':
        if len(myqueue) == 0:
            print(-1)

        else:
            print(myqueue[-1])

    else:
        integer = int(command[1])
        myqueue.append(integer)

# 그냥 input으로 command를 받으면 시간초과가 났다.
# 시간초과 해결 방법
# 1. sys.stdin.readline()을 이용하기
# 2. deque를 활용하기