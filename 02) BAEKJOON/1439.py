num = input()
num_list = list(num)
new_num_list = [num_list[0]]

for i in range(len(num_list)):
    if i == 0:
        continue

    if num_list[i] != num_list[i - 1]:
        new_num_list.append(num_list[i])

zero_count = new_num_list.count("0")
one_count = new_num_list.count("1")
print(min(zero_count, one_count))