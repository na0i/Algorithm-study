def multiply(arr):
    num = 1

    for n in arr:
        num *= n

    return num


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    M_list = [i for i in range(M, M - N, -1)]
    N_list = [j for j in range(N, 0, -1)]

    print(multiply(M_list) // multiply(N_list))