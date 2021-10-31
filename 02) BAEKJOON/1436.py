N = int(input())
maxx = 987654321
num_666 = []

for i in range(666, maxx):
    str_num = str(i)
    for j in range(len(str_num)-2):
        if str_num[j] == '6' and str_num[j+1] == '6' and str_num[j+2] == '6':
            num_666.append(str_num)
            break

    if len(num_666) == N:
        break

print(num_666[N-1])