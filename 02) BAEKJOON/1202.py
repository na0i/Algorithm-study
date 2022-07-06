from collections import deque

N, K = map(int, input().split())
jewelry = []
K_list = []
for _ in range(N):
    M, V = map(int, input().split())
    jewelry.append([V, M])

sorted_jewelry = sorted(jewelry)
sorted_jewelry.reverse()
sorted_jewelry = deque(sorted_jewelry)

for i in range(K):
    K_list.append(int(input()))

sorted_k_list = sorted(K_list)
sorted_k_list.reverse()

k_idx = 0
answer = 0
print(sorted_jewelry, sorted_k_list)
while sorted_jewelry and k_idx < K:
    now_jewelry = sorted_jewelry.popleft()
    can_carry = sorted_k_list[k_idx]
    if now_jewelry[1] > can_carry:
        continue
    else:
        k_idx += 1
        answer += now_jewelry[0]
        print(now_jewelry[0])

print(answer)