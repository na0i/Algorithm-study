find_num = int(input())
M = int(input())
broken = []
if M:
    broken = list(map(str, input().split()))

if find_num == 100:
    print(0)

elif len(broken) == 10:
    print(abs(find_num - 100))

else:
    num_1 = find_num
    num_2 = find_num
    cnt = 0
    answer = 0

    while True:
        num_1 = str(num_1)
        num_2 = str(num_2)
        is_num1_broken = False
        is_num2_broken = False

        for i in num_1:
            if i in broken:
                is_num1_broken = True
                break

        for j in num_2:
            if j in broken:
                is_num2_broken = True
                break

        if not is_num1_broken and not is_num2_broken:
            min_len = min(len(num_1), len(num_2))
            answer += min_len + cnt
            break

        elif not is_num1_broken:
            answer = len(num_1) + cnt
            break

        elif not is_num2_broken:
            answer = len(num_2) + cnt
            break

        elif is_num1_broken and is_num2_broken:
            cnt += 1
            num_1 = int(num_1) + 1
            num_2 = int(num_2) - 1

    print(min(answer, abs(find_num - 100)))