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


# 어차피 분해합은 N보다는 작을테니까
# N까지 브루트포스를 이용해서 탐색하면 된다.