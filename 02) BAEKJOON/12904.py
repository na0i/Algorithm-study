origin = input()
new = list(input())

while len(new) != len(origin):
    if new[-1] == 'A':
        new.pop(-1)
    else:
        new.pop(-1)
        new.reverse()

compare = ''
for i in new:
    compare += i

if origin == compare:
    print(1)
else:
    print(0)