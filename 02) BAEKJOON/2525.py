hour, minute = map(int, input().split())
time = int(input())


if minute + time < 60:
    print(hour, minute + time)

else:
    temp_hour = (minute + time) // 60
    temp_minute = (minute + time) % 60

    hour += temp_hour
    minute = temp_minute

    if hour == 24:
        hour = 0

    elif hour > 24:
        share = hour // 24
        hour -= 24 * share

    print(hour, minute)