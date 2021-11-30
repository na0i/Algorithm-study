N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list = sorted(N_list)

for target in M_list:
    flag = False
    start = 0
    end = N - 1

    while start <= end:
        middle = (start + end) // 2
        if N_list[middle] == target:
            flag = True
            break
        elif N_list[middle] < target:
            start = middle + 1
        elif N_list[middle] > target:
            end = middle - 1

    if flag == True:
        print('1')
    else:
        print('0')