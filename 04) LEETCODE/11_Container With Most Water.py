height = [1,8,6,2,5,4,8,3,7]
sorted_height = sorted(height, reverse=True)
idx_height_dict = {}

for i in range(len(height)):
    idx_height_dict[i] = height[i]

idx_height_dict = sorted(idx_height_dict.items(), key=lambda x : x[1], reverse=True)

# idx_height_dict = {0: 1, 1: 8, 2: 6, 3: 2, 4: 5, 5: 4, 6: 8, 7: 3, 8: 7}
# idx_height_dict = [(1, 8), (6, 8), (8, 7), (2, 6), (4, 5), (5, 4), (7, 3), (3, 2), (0, 1)]
# print(idx_height_dict)

idx_diff = 0
h = 0
answer = 0

for i in range(len(height)):
    left_idx = idx_height_dict[i][0]
    left_height = idx_height_dict[i][1]

    for j in range(len(height)):
        right_idx = idx_height_dict[j][0]
        right_height = idx_height_dict[j][1]

        idx_diff = abs(left_idx - right_idx)
        h = min(left_height, right_height)

        if idx_diff * h > answer:
            answer = idx_diff * h

        else:
            break

print(answer)

