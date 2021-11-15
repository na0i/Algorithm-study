num = input()
answer = int(num)
for i in range(int(num), 987654321):
    if i % 2 != 0:
        pass
    else:
        length = len(str(num))
        if length % 2 != 0:
            pass
        else:
            front = str(i)[0:length//2]
            back = str(i)[length//2:length+1]
            front_mul = 1
            back_mul = 1
            for m in range(length//2):
                front_mul *= int(str(front)[m])
                back_mul *= int(str(back)[m])

            if front_mul == back_mul:
                if int(i) >= answer:
                    answer = i
                    break

print(answer)