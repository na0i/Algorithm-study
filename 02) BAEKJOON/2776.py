T = int(input())


def find_num(arr, target):
    start = 0
    end = len(arr) - 1
    flag = 0

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            flag = 1
            break

    return flag


for tc in range(T):
    N = int(input())
    diary_1 = list(map(int, input().split()))
    diary_1.sort()
    M = int(input())
    diary_2 = list(map(int, input().split()))

    for num in diary_2:
        print(find_num(diary_1, num))