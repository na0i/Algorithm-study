find_num = int(input())
broken_cnt = int(input())
broken_list = list(input().split())

remote = [str(_) for _ in range(10)]

for b in broken_list:
    remote.remove(b)


def is_broken(strr):
    flag = False

    for l in strr:
        for bl in broken_list:
            if l == bl:
                flag = True
                break

    return flag


plus_find_num = int(find_num)
minus_find_num = int(find_num)
answer = 987654321

while True and find_num != 100:
    plus_find_num += 1
    minus_find_num -= 1

    if not is_broken(str(plus_find_num)):
        answer = abs(int(plus_find_num) - find_num)
        break

    elif not is_broken(str(minus_find_num)):
        answer = abs(int(minus_find_num) - find_num)
        break

print(plus_find_num, minus_find_num, answer)
