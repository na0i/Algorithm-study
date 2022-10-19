sugar = int(input())
cnt_5 = sugar // 5
cnt_3 = 0
remaining = sugar % 5

while cnt_5 >= 0:

    if remaining % 3 == 0:
        cnt_3 = remaining // 3
        break

    else:
        cnt_5 -= 1
        remaining += 5


if cnt_5 == -1 or cnt_3 == -1:
    print(-1)
else:
    print(cnt_5 + cnt_3)