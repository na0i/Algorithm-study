p = [6, 2, 1, 0, 2, 4, 3]
c = [3, 6, 6, 2, 3, 7, 6]
n = 7

possible = 0
cost = 100
total = []
cannot = 0
dates = 0
fail = False
for i in range(n):
    possible += p[i]
    if possible >= c[i]:
        possible -= c[i]
        total.append(cost*c[i])
        cost = 100
    else:
        cannot += 1
        cost //= 2
        total.append(0)

    if cannot == 4:
        dates = i + 1
        break
    dates = i+1

answer = sum(total) // dates
print('{:.2f}'.format(round(sum(total) // dates, 2)))