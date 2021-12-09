import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = deque()
stack.append(A[0])

for i in range(1, N):
