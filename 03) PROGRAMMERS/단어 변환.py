from collections import deque


def find_different_cha_count(str1, str2):
    diff_count = 0
    for a, b in zip(str1, str2):
        if a != b:
            diff_count += 1

    return diff_count


def solution(begin, target, words):
    answer = 0
    visited = {begin: 0}
    queue = deque([begin])

    while queue:
        now_word = queue.popleft()

        if now_word == target:
            answer = visited[target]
            break

        for new_word in words:
            if new_word not in visited and find_different_cha_count(now_word, new_word) == 1:
                queue.append(new_word)
                visited[new_word] = visited[now_word] + 1
    return answer