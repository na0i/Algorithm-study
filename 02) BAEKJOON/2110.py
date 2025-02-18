house, router = map(int, input().split())
house_position = []
for i in range(house):
    house_position.append(int(input()))

house_position.sort()

start, end = 1, house_position[-1] - house_position[0]
answer = 1
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    installed = [1]
    last_installed = house_position[0]
    for i in range(1, house):
        if last_installed + mid > house_position[i]:
            continue
        else:
            cnt += 1
            last_installed = house_position[i]
            installed.append(house_position[i])

    if cnt >= router:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1


print(answer)