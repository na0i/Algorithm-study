N = int(input())
chain = sorted(list(map(int, input().split())))

cnt = 0

while chain:
    can_tie = chain[0]
    chain = chain[1:]

    if len(chain) == can_tie + 1:
        cnt += can_tie
        chain = chain[:-can_tie]

    else:
        while can_tie and chain:
            can_tie -= 1
            chain.pop()
            cnt += 1

print(cnt)