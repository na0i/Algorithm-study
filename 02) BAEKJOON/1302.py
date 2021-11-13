N = int(input())
book_list = []
for i in range(N):
    book = input()
    book_list.append(book)

sorted_list = sorted(book_list)
print(sorted_list)
cnt = 1
answer = ''
for i in range(1, N):
    if sorted_list[i] != sorted_list[i-1]:
        new_cnt = 1
        if cnt > new_cnt:
            answer = sorted_list[i-1]
        else:
            answer = sorted_list[i]

    else:
        cnt += 1

print(answer)