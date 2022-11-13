gear_one = list(input())
gear_two = list(input())
gear_three = list(input())
gear_four = list(input())
gear_list = [[0], gear_one, gear_two, gear_three, gear_four]


def turn_left(lst):
    tmp = lst.pop(0)
    lst.append(tmp)
    return lst


def turn_right(lst):
    tmp = lst.pop()
    lst = [tmp] + lst
    return lst


K = int(input())
for k in range(K):
    idx, dir = map(int, input().split())

    check = [0, 0, 0, 0, 0]  # 바꿀 기어 index 확인 list
    check[idx] = dir

    current_idx = idx
    left_idx = idx - 1
    right_idx = idx + 1

    while 0 < left_idx <= 4:
        if gear_list[current_idx][6] == gear_list[left_idx][2]:
            break
        else:
            check[left_idx] = check[current_idx] * (-1)
            current_idx -= 1
            left_idx -= 1

    for i in range(5):
        if i == idx:
            continue
        elif check[i] == -1:
            gear_list[i] = turn_left(gear_list[i])
        elif check[i] == 1:
            gear_list[i] = turn_right(gear_list[i])
        else:
            continue

    current_idx = idx
    check = [0, 0, 0, 0, 0]
    check[idx] = dir

    while 0 < right_idx <= 4:
        if gear_list[current_idx][2] == gear_list[right_idx][6]:
            break
        else:
            check[right_idx] = check[current_idx] * (-1)
            current_idx += 1
            right_idx += 1

    for i in range(5):
        if i == idx:
            continue
        elif check[i] == -1:
            gear_list[i] = turn_left(gear_list[i])
        elif check[i] == 1:
            gear_list[i] = turn_right(gear_list[i])
        else:
            continue

    if dir == -1:
        gear_list[idx] = turn_left(gear_list[idx])
    else:
        gear_list[idx] = turn_right(gear_list[idx])


answer = 0
for i in range(1, 5):
    if gear_list[i][0] == '1':
        answer += 2 ** (i-1)

print(answer)