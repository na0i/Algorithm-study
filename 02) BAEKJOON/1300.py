import sys
N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
N_dict = {}
key = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        key += 1
        N_dict[key] = i * j

sorted_N_dict = sorted(N_dict.items(), key=lambda x: x[1])

llist = []
for i in sorted_N_dict:
    llist.append(i[1])

print(llist[K-1])