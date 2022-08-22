numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
prerequisites_list = [[0] * numCourses for _ in range(numCourses)]
visited = [0] * numCourses
global result
result = True


def bfs():
    global result

    while stack:
        now = stack.pop(0)
        for k in range(numCourses):
            if prerequisites_list[now][k] == 1 and visited[k] == 1:
                result = False
                break
            elif prerequisites_list[now][k] == 1 and visited[k] == 0:
                stack.append(k)
                visited[k] = 1


for req in prerequisites:
    prerequisites_list[req[0]][req[1]] = 1

for i in range(numCourses):
    if 1 in prerequisites_list[i]:
        stack = [i]
        visited[i] = 1
        bfs()
        break

for v in visited:
    if v == 0:
        result = False

print(result)