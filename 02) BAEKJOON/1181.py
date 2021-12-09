N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)

set_sorted_words = sorted(set(words), key=lambda x: (len(x), x[:]))
for w in set_sorted_words:
    print(w)