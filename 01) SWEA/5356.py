import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())
for tc in range(T):
    words = [list(input()) for _ in range(5)]

    words_length = []
    for i in range(5):
        words_length.append(len(words[i]))

    for i in range(5):
        if len(words[i]) < max(words_length):
            words[i] += ' ' * (max(words_length) - len(words[i]))

    answer = ''
    for i in range(len(words[0])):
        for j in range(5):
            answer += words[j][i]

    print('#{} {}'.format(tc+1, answer.replace(' ', '')))