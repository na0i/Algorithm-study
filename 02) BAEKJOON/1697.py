from collections import deque


def walk_go(x):
    x += 1
    return x


def walk_back(x):
    x -= 1
    return x


def teleport(x):
    x *= 2
    return x


N, K = map(int, input().split())
visited = [0] * 100001
queue = deque()

queue.append(N)

while queue:
    now = queue.popleft()

    if now == K:
        print(visited[K])
        break

    for i in (walk_go(now), walk_back(now), teleport(now)):
        next = i

        if 0 <= next < 100001 and visited[next] == 0:
            visited[next] = visited[now] + 1
            queue.append(next)


# visited를 [0] * 100000이라고 했더니 런타임에러(indexError)가 났다.
# if now == K 문이 for문보다 먼저 등장하지 않으면 틀린다는 것도 유의한다.