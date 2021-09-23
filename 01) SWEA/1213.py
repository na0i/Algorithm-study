import sys
sys.stdin = open('1213.txt', 'r', encoding='UTF8')

for tc in range(10):
    test_num = int(input())
    word = input()
    sentence = list(input())

    answer = 0
    for i in range(len(sentence) - len(word) + 1):
        idx = 0
        while idx < len(word) and sentence[i+idx] == word[idx]:
            idx += 1

        if idx == len(word):
            answer += 1

    print('#{} {}'.format(test_num, answer))

