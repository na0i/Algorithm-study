N = int(input())
fibonacci = [0] * (N + 1)
if N >= 1:
    fibonacci[1] = 1
idx = 2

while idx <= N:
    fibonacci[idx] = fibonacci[idx - 2] + fibonacci[idx - 1]
    idx += 1

print(fibonacci[N] % 1000000007)
