N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start = 1
end = sum(lectures)
longest = max(lectures)

while start <= end:
    bluray_size = (start + end) // 2
    temp_cnt = 1
    temp_size = 0

    for lecture in lectures:
        if temp_size + lecture <= bluray_size:
            temp_size += lecture

        else:
            temp_cnt += 1
            temp_size = lecture

    if temp_cnt > M:
        start = bluray_size + 1

    else:
        end = bluray_size - 1

print(max(longest, start))

# 찾은 값이 bluray size 보다 작을 경우를 생각 못했다.
# 찾은 값이 400일 때 길이가 500인 강의는 담을 수 없다.
