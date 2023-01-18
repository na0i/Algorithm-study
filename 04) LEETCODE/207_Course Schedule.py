from collections import deque

numCourses = 6
# prerequisites = [[1, 0]]
# prerequisites = [[1, 0], [0, 1]]
prerequisites = [[1, 2], [3, 5], [4, 5]]
link_list = [[] for _ in range(numCourses)]
for req in prerequisites:
    start = req[0]
    end = req[1]
    link_list[start].append(end)


answer = True
for i in range(len(link_list)):
    link = link_list[i]
    if len(link) > 0 and answer:
        start = link[0]
        queue = deque()
        queue.append(link[0])
        visited = [False for _ in range(numCourses)]

        while queue:
            now = queue.popleft()
            print(link, now, start, i)
            if now == i:
                answer = False
                break
            else:
                visited[now] = True

                for l in link_list[now]:
                    if not visited[l]:
                        queue.append(l)

print(answer)