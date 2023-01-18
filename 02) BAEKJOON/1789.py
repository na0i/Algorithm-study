S = int(input())

sub_sum = 0
now = 1
cnt = 0
while True:
    if sub_sum == S:
        break
    elif sub_sum > S:
        cnt -= 1
        break
    else:
        sub_sum += now
        now += 1
        cnt += 1

print(cnt)
