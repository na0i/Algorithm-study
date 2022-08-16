N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes = sorted(ropes, reverse=True)
result = []

for cnt in range(len(ropes)):
    can_hold = ropes[cnt] * (cnt+1)
    result.append(can_hold)

print(max(result))