import sys
sys.stdin = open('1219.txt', 'r')

for tc in range(10):
    test_case, length = map(int, input().split())
    link = list(map(int, input().split()))
    way = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(0, length*2, 2):
        way[link[i]][link[i+1]] = 1


    def find_way():
        stack = [0]
        while stack:
            start = stack.pop(0)
            for i in range(100):
                if way[start][i] == 1:
                    if i == 99:
                        return 1
                    else:
                        stack.append(i)
        return 0

    print('#{} {}'.format(test_case, find_way()))