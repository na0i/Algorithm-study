import sys
sys.stdin = open('1225.txt', 'r')

for tc in range(10):
    test_case = int(input())
    password = list(map(int, input().split()))

    minus = [5, 1, 2, 3, 4]
    turn = 1
    num = password.pop(0) - 1

    while num > 0:
        password.append(num)
        turn += 1

        cycle = turn % 5

        num = password.pop(0) - minus[cycle]
        if num <= 0:
            password.append(0)
            break

    print('#{} {} {} {} {} {} {} {} {}'.format(test_case, password[0], password[1], password[2], password[3], password[4], password[5], password[6], password[7]))