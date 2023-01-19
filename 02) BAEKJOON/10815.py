N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cards.sort()


def binary_search(arr, start, end, target):

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1

        elif arr[mid] > target:
            end = mid - 1

        elif arr[mid] < target:
            start = mid + 1

    return 0


result = []
for num in nums:
    isExist = binary_search(cards, 0, len(cards) - 1, num)
    result.append(isExist)

for r in result:
    print(r, end=' ')