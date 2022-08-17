from itertools import combinations

T = int(input())
for tc in range(T):
    num_clothes = int(input())

    dict_clothes = {}
    category_list = []
    for _ in range(num_clothes):
        name, category = input().split()
        if category not in category_list:
            category_list.append(category)
            dict_clothes[category] = [name]
        else:
            dict_clothes[category].append(name)

    # dict_clothes = {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}

    cnt_clothes = []
    for category in category_list:
        cnt_clothes.append(len(dict_clothes[category]))

    # cnt_clothes = [2, 1]

    result = 1
    for cnt in cnt_clothes:
        result *= cnt + 1   # cnt + 1: 안입는 경우도 포함

    print(result - 1)   # result - 1: 아무것도 안입는 경우 제외