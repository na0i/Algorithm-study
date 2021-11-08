T = int(input())

for tc in range(T):
    p = list(input())
    n = int(input())

    if n != 0:
        n_list = input()
        n_list = n_list[1:len(n_list)-1]
        n_list = n_list.split(',')

        for i in range(len(p)):
            if p[i] == 'R':
                n_list.reverse()

            elif p[i] == 'D':
                n_list.pop(0)

            if len(n_list) == 0:
                print('error')
                break

        if len(n_list) != 0:
            result = []
            for j in range(len(n_list)):
                result.append(int(n_list[j]))

            print(result)

    else:
        n_list = input()
        print('error')