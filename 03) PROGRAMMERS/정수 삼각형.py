def solution(triangle):
    sum_triangle = []
    for i in range(len(triangle)):
        temp = []
        for j in range(len(triangle[i])):
            if i == 0 and j == 0:
                temp.append(triangle[0][0])
            else:
                if j == 0:
                    temp.append(sum_triangle[i - 1][j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    temp.append(sum_triangle[i - 1][j - 1] + triangle[i][j])
                else:
                    temp.append(
                        max(sum_triangle[i - 1][j - 1] + triangle[i][j], sum_triangle[i - 1][j] + triangle[i][j]))

        sum_triangle.append(temp)

    answer = 0
    for i in range(len(sum_triangle)):
        answer = max(answer, max(sum_triangle[i]))

    return answer

