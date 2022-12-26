# pairs = [[1, 2], [2, 3], [3, 4]]
# pairs = [[1, 2], [7, 8], [4, 5]]
pairs = [[1, 7],  [2, 3],  [3, 7],  [8, 9]]
# pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
pairs.sort()
pairs.reverse()

now = pairs[0]
cnt = 1

for i in range(1, len(pairs)):
    print(now, now[0], pairs[i][1])
    if now[0] <= pairs[i][1]:
        continue
    else:
        now = pairs[i]
        cnt += 1

print(cnt)