gear_one = list(input())
gear_two = list(input())
gear_three = list(input())
gear_four = list(input())
gear_list = [gear_one, gear_two, gear_three, gear_four]

K = int(input())
for k in range(K):
    gear_idx, dirr = map(int, input().split())

    gear_idx -= 1
    left_idx = gear_idx - 1
    right_idx = gear_idx + 1

    while left_idx >= 0:
        # 회전 톱니 바퀴의 6번째 바퀴와 좌측 톱니 바퀴의 2번째 바퀴의 방향이 같을 때
        # 회전 톱니 바퀴만 회전
        if gear_list[left_idx][2] == gear_list[gear_idx][6]:
            if dirr == -1:  # 반시계 방향 회전
                temp = gear_list[gear_idx].pop(0)
                gear_list[gear_idx].append(temp)

            else:  # 시계 방향 회전
                temp = gear_list[gear_idx].pop()
                gear_list[gear_idx] = [temp] + gear_list[gear_idx]

        # 회전 톱니 바퀴의 6번째 바퀴와 좌측 톱니 바퀴의 2번째 바퀴의 방향이 다를 때
        # 회전 톱니 바퀴와 좌측 톱니 바퀴 모두 회전
        else:
            if dirr == -1:
                temp = gear_list[gear_idx].pop(0)
                gear_list[gear_idx].append(temp)

                temp = gear_list[left_idx].pop()
                gear_list[left_idx] = [temp] + gear_list[left_idx]

            else:
                temp = gear_list[gear_idx].pop()
                gear_list[gear_idx] = [temp] + gear_list[gear_idx]

                temp = gear_list[left_idx].pop(0)
                gear_list[left_idx].append(temp)

        # 왼쪽으로 이동하며 반복
        left_idx -= 1
        gear_idx -= 1

    # gear_idx 초기화
    gear_idx = right_idx - 1

    # 우측도 동일한 원리
    while right_idx < 4:
        if gear_list[right_idx][6] == gear_list[gear_idx][2]:
            if dirr == -1:
                temp = gear_list[gear_idx].pop(0)
                gear_list[gear_idx].append(temp)

            else:
                temp = gear_list[gear_idx].pop()
                gear_list[gear_idx] = [temp] + gear_list[gear_idx]

        else:
            if dirr == -1:
                temp = gear_list[gear_idx].pop(0)
                gear_list[gear_idx].append(temp)

                temp = gear_list[right_idx].pop()
                gear_list[right_idx] = [temp] + gear_list[right_idx]

            else:
                temp = gear_list[gear_idx].pop()
                gear_list[gear_idx] = [temp] + gear_list[gear_idx]

                temp = gear_list[right_idx].pop(0)
                gear_list[right_idx].append(temp)

        right_idx += 1
        gear_idx += 1

    for j in range(4):
        print(gear_list[j])


answer = 0
for i in range(4):
    if gear_list[i][0] == '1':
        answer += 2 ** i

print(answer)