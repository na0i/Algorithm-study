N, M = map(str, input().split())
rev_N = ''
rev_M = ''

for i in range(len(N)-1, -1, -1):
    rev_N += N[i]

for j in range(len(M)-1, -1, -1):
    rev_M += M[j]

if int(rev_N) >= int(rev_M):
    print(rev_N)
else:
    print(rev_M)