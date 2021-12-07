# N = int(input())
# left = [0] * (N+1)
# right = [0] * (N+1)
# parent = [0] * (N+1)
# for n in range(N-1):
#     s, e = map(int, input().split())
#
#     if parent[e] == 1:
#         s, e = e, s
#
#     if e == 1:
#         s, e = e, s
#
#     if left[s] != 0:
#         right[s] = e
#         parent[e] = 1
#
#     else:
#         left[s] = e
#         parent[e] = 1
#
# result = []
# for i in range(N+1):
#     if left[i] != 0:
#         result.append((left[i], i))
#
#     if right[i] != 0:
#         result.append((right[i], i))
#
# result = sorted(result)
# for j in range(len(result)):
#     print(result[j][1])
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [([] * (N+1)) for _ in range(N+1)]
parent = [0] * (N+1)

def bfs():
    myQ = deque()
    myQ.append(1)
    while myQ:
        now = myQ.popleft()
        for i in tree[now]:
            if not parent[i]:
                myQ.append(i)
                parent[i] = now
    return parent


for n in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


bfs()
for p in range(2, N+1):
    print(parent[p])