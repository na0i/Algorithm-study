import copy
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    my_queue = deque(queue)
    current_idx = M
    cnt = 1

    if len(my_queue) == 1:
        print(1)

    else:
        while len(my_queue) > 1:
            now = my_queue.popleft()
            check = sorted(copy.deepcopy(my_queue), reverse=True)[0]    # 나보다 뒤에 있는 것들 중에 제일 큰 애
            if check <= now and current_idx == 0:    # 다 나보다 작고 내가 맨 앞일 때
                print(cnt)
                break

            elif check <= now and current_idx != 0:
                cnt += 1

            else:
                my_queue.append(now)    # 다시 뒤에 추가

            current_idx -= 1
            if current_idx < 0:
                current_idx = len(my_queue) - 1

            if len(my_queue) == 1:
                print(cnt)
                break