N = int(input())
cards = [input() for _ in range(N)]
alphabet = {}

max_len = 0
for i in range(N):
    if len(cards[i]) > max_len:
        max_len = len(cards[i])

for i in range(N):
    if len(cards[i]) < max_len:
        for j in range(max_len - len(cards[i])):
            cards[i] = '0' + cards[i]

for i in range(N):
    for j in range(max_len):
        if cards[i][j] == '0':
            continue
        elif cards[i][j] in alphabet:
            alphabet[cards[i][j]] += 10 ** (max_len - j - 1)
        else:
            alphabet[cards[i][j]] = 10 ** (max_len - j - 1)

sorted_alphabet = sorted(alphabet.items(), key=lambda x:x[1], reverse=True)
card_number_pair = {}
number = 9
for i in range(len(sorted_alphabet)):
    card_number_pair[sorted_alphabet[i][0]] = number
    number -= 1

card_sum = 0
for i in range(N):
    for j in range(max_len):
        if cards[i][j] == '0':
            continue
        else:
            card_sum += card_number_pair[cards[i][j]] * (10 ** (max_len - j - 1))

print(card_sum)
