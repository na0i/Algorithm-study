from collections import deque

def solution(numbers, target):

    queue = deque([0])
    for num in numbers:
        temp = []

        while queue:
            now = queue.popleft()
            temp.append(now + num)
            temp.append(now - num)

        queue = deque(temp)

    return queue.count(target)