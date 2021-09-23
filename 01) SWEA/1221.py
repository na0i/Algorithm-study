import sys
sys.stdin = open('1221.txt', 'r')

T = int(input())

for tc in range(T):
    tc, tc_length = map(str, input().split())
    galaxy_str = list(input().split())

    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''

    for i in range(int(tc_length)):
        if galaxy_str[i] == 'ZRO':
            zero += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'ONE':
            one += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'TWO':
            two += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'THR':
            three += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'FOR':
            four += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'FIV':
            five += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'SIX':
            six += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'SVN':
            seven += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'EGT':
            eight += galaxy_str[i] + ' '
        elif galaxy_str[i] == 'NIN':
            nine += galaxy_str[i] + ' '


    answer = zero + one + two + three + four + five + six + seven + eight + nine

    print('{} {}'.format(tc, answer))