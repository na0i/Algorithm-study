N = int(input())
left = [0] * (N+1)
right = [0] * (N+1)
parent = [0] * (N+1)
for n in range(N-1):
    s, e = map(int, input().split())

    if e == 1:
        s, e = e, s

    if left[s] != 0:
        right[s] = e
        parent[e] = 1
    else:
        left[s] = e
        parent[e] = 1


print(left)
print(right)