T = int(input())

for tc in range(T):
    N = int(input())

    fibonacci = [[] for _ in range(41)]
    fibonacci[0] = [1, 0]
    fibonacci[1] = [0, 1]

    if N >= 2:
        for n in range(2, N + 1):
            cnt_0 = fibonacci[n-2][0] + fibonacci[n-1][0]
            cnt_1 = fibonacci[n-2][1] + fibonacci[n-1][1]

            fibonacci[n] = [cnt_0, cnt_1]

    print(fibonacci[N][0], fibonacci[N][1])