n = 402
my_stack = [True for _ in range(99999)]

idx_2 = 2
idx_3 = 3
idx_5 = 5
idx_6 = 6
idx_10 = 10
idx_15 = 15

while idx_2 < 99999:
    my_stack[idx_2] = False
    idx_2 *= 2


while idx_3 < 99999:
    my_stack[idx_3] = False
    idx_3 *= 3


while idx_5 < 99999:
    my_stack[idx_5] = False
    idx_5 *= 5

while idx_6 < 99999:
    my_stack[idx_6] = False
    idx_6 *= 6

while idx_10 < 99999:
    my_stack[idx_10] = False
    idx_10 *= 10

while idx_15 < 99999:
    my_stack[idx_15] = False
    idx_15 *= 15


print(my_stack[0:50])
result = [1]
for i in range(len(my_stack)):
    if my_stack[i] == False:
        result.append(i)

print(result)