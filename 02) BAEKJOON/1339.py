from collections import Counter

N = int(input())
words_list = [list(input()) for _ in range(N)]
cnt_check_list = [list() for _ in range(10)]
sorted_words_list = sorted(words_list, key=lambda x:len(x))
sorted_words_list.reverse() # 단어가 긴 순으로 정렬

print(sorted_words_list)
for i in range(len(sorted_words_list)):
    word_length = len(sorted_words_list[i])
    for j in range(word_length):
        cnt_check_list[word_length-j-1].append(sorted_words_list[i][j])

print(cnt_check_list)
# [['B', 'F'], ['E', 'C'], ['D', 'G'], ['C'], ['A'], [], [], [], [], []]

number_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
result = []
for i in range(9, -1, -1):
    if len(cnt_check_list[i]) == 0:
        continue
    else:
        counts = Counter(cnt_check_list[i])
        for key, value in range(1):
            print(counts[key])
            # now_number = number_list.pop()
            # result.append([key, now_number])

print(result)