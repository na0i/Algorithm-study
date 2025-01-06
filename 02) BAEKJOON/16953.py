A, B = map(int, input().split())

count = 0
flag = True
while flag:
    if A == B:
        print(count + 1)
        break
    elif B < A:
        print(-1)
        break
    elif B % 2 == 0:
        B = B // 2
        count += 1
        continue
    elif str(B)[-1] == "1":
        B = int(str(B)[0:-1])
        count += 1
        continue
    else:
        print(-1)
        break

