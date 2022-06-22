not_self_number = []
for i in range(10000):
    str_num = str(i)
    str_num_sum = int(str_num)
    for j in range(len(str_num)):
        str_num_sum += int(str_num[j])
    not_self_number.append(str_num_sum)

not_self_number = sorted(not_self_number)
for i in range(10000):
    if i not in not_self_number:
        print(i)