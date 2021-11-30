# calcul = list(input())
# calcul_list = []
# sign = ['+', '-']
#
# num = ''
# for i in range(len(calcul)):
#     if calcul[i] != sign[0] and calcul[i] != sign[1]:
#         num += calcul[i]
#     else:
#         calcul_list.append(num)
#         calcul_list.append(calcul[i])
#         num = ''
#     if i == len(calcul) - 1:
#         calcul_list.append(num)
#
# gwalho = ['(', ')']

calcul = list(map(str, input().split('-')))

answer = 0
first = 0
sub = 0
for c in range(1):
    num = calcul[c].split('+')
    for n in range(len(num)):
        first += int(num[n])

for c in range(1, len(calcul)):
    num = calcul[c].split('+')
    for n in range(len(num)):
        sub += int(num[n])

answer = answer + first - sub
print(answer)