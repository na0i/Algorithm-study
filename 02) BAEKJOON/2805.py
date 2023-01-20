N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 1
end = sum(trees)
target = M

while start <= end:
    cut_height = (start + end) // 2
    cut_sum = 0
    for tree in trees:
        cut_sum += max(tree - cut_height, 0)

    if cut_sum >= target:
        start = cut_height + 1

    elif cut_sum < target:
        end = cut_height - 1

print(end)

# 파라메트릭서치는 이분탐색을 이용할 수는 있지만
# 값 내에서 값을 찾는게 아니라
# 범위 내에서 최적 값을 찾는다.
# 따라서, cut_sum == target: break 와 같은 식으로 동작하지 않는다.
# start, end의 범위
# 종료조건에 유의하자.