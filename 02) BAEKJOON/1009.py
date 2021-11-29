T = int(input())
for tc in range(T):
    a, b = map(int, input().split())

    # data = pow(a, b)
    # data = str(data)
    #
    # if data[-1] == '0':
    #     print('10')
    # else:
    #     print(data[-1])

    nameoji = 1
    for i in range(b):
        nameoji = (a * nameoji) % 10

    if nameoji == 0:
        print(10)
    else:
        print(nameoji)