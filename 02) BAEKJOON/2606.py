def conta_comp(road, start):
    global answer
    answer += 1
    visited[start] = 1

    for i in range(len_all_comp+1):
        if visited[i] != 1 and road[start][i] == 1:
            conta_comp(road, i)

    return answer

len_all_comp = int(input())
len_linked_comp = int(input())
computers = [[0] * (len_all_comp + 1) for _ in range(len_all_comp + 1)]
visited = [0] * (len_all_comp + 1)
answer = 0

for i in range(len_linked_comp):
    a, b = map(int, input().split())
    computers[a][b] = 1
    computers[b][a] = 1


conta_comp(computers, 1)
print(answer - 1)