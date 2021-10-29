def sub_sum(x):
    result = x
    for i in range(len(str(x))):
        result += int(str(x)[i])

    return result


N = input()

flag = False
for n in range(int(N)):
    if sub_sum(n) == int(N):
        flag = True
        break

if flag:
    print(n)

else:
    print(0)
