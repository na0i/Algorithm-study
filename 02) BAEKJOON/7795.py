T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A_list.sort()
    B_list.sort()
    A_list.reverse()
    B_list.reverse()

    cnt = 0
    for a_idx in range(len(A_list)):
        for b_idx in range(len(B_list)):
            a = A_list[a_idx]
            b = B_list[b_idx]

            if a > b:
                cnt += M - b_idx
                break

    print(cnt)