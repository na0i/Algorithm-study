calcul = list(input())
calcul_list = []
sign = ['+', '-']

num = ''
for i in range(len(calcul)):
    if calcul[i] != sign[0] and calcul[i] != sign[1]:
        num += calcul[i]
    else:
        calcul_list.append(num)
        calcul_list.append(calcul[i])
        num = ''
    if i == len(calcul) - 1:
        calcul_list.append(num)

gwalho = ['(', ')']

