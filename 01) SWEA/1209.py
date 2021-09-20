import sys
sys.stdin = open('1209.txt', 'r')

for tc in range(10):
    tc_num = int(input())

    nums = []
    for row in range(100):
        row_num = list(map(int, input().split()))
        nums.append(row_num)

    max_total = 0

    for r in range(100):
        if sum(nums[r]) > max_total:
            max_total = sum(nums[r])

    diag_num_1 = []
    diag_num_2 = []
    for d in range(100):
        diag_num_1.append(nums[d][d])
        diag_num_2.append(nums[d][99-d])

    if sum(diag_num_1) > max_total:
        max_total = sum(diag_num_1)

    if sum(diag_num_2) > max_total:
        max_total = sum(diag_num_2)

    all_col_num = []
    for r in range(100):
        col_num = []
        for c in range(100):
            col_num.append(nums[c][r])
        all_col_num.append(col_num)

    for c in range(100):
        if sum(all_col_num[c]) > max_total:
            max_total = sum(all_col_num[c])

    print('#{} {}'.format(tc_num, max_total))
