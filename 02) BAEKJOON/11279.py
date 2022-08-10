import sys
import heapq    # 우선순위 큐 구현을 위해 priorityQueue를 사용하는 것보다 heapQ가 낫다
N = int(sys.stdin.readline())
priorityQ = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 and len(priorityQ) == 0:
        print(0)
    elif n == 0 and len(priorityQ) != 0:
        print(heapq.heappop(priorityQ)[1])
    else:
        # 우선순위 큐는 기본적으로 최소힙이 구현되므로 앞에 음수를 붙임으로써 최대힙으로 구현
        heapq.heappush(priorityQ, (-n, n))
