N = int(input())
ropes = []
for n in range(N):
    ropes.append(int(input()))

sorted_ropes = sorted(ropes)
sorted_ropes.reverse()

result = sorted_ropes[0]
for i in range(N):
    use_ropes = i + 1
    handle_weight = sorted_ropes[i] * use_ropes
    if handle_weight > result:
        result = handle_weight

print(result)