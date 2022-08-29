rectangles = [[5,8],[3,9],[5,12],[16,5]]
min_len_list = []

for rect in rectangles:
    min_len_list.append(min(rect))

min_len_list = sorted(min_len_list)
max_len = min_len_list[-1]
max_len_idx = 0

for i in range(len(min_len_list)-1, -1, -1):
    if min_len_list[i] != max_len:
        max_len_idx = i
        break

if len(min_len_list) > 1:
    print(len(min_len_list) - (max_len_idx + 1))
else:
    print(min(rectangles[0]))