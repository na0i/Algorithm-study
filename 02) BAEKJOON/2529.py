import sys
K = int(sys.stdin.readline())
inequality_list = list(map(str, sys.stdin.readline().split()))
visited = [0] * 10
inequality_idx = 0  # 부등호 리스트 index(하나씩 늘려가며 부등호 좌측 숫자랑 비교하려고)
num_str = ''
result = []


def backtracking():
    global inequality_idx
    global num_str

    if len(num_str) == len(inequality_list) + 1:  # 종료 조건
        result.append(num_str)
        return

    for i in range(10):
        if inequality_list[inequality_idx] == '<':
            if int(num_str[-1]) < i and visited[i] == 0:  # 부등호 조건을 만족하면서 방문하지 않았을 경우
                num_str += str(i)
                visited[i] = 1
                inequality_idx += 1
                backtracking()
                num_str = num_str[:-1]
                visited[i] = 0
                inequality_idx -= 1

        if inequality_list[inequality_idx] == '>':
            if int(num_str[-1]) > i and visited[i] == 0:   # 부등호 조건을 만족하면서 방문하지 않았을 경우
                num_str += str(i)
                visited[i] = 1
                inequality_idx += 1
                backtracking()
                num_str = num_str[:-1]
                visited[i] = 0
                inequality_idx -= 1


for start_num in range(10):     # 첫번째 숫자 정하기
    num_str += str(start_num)
    visited[start_num] = 1
    backtracking()  # 백트래킹 시작
    num_str = num_str[:-1]
    visited[start_num] = 0


print(result[-1])  # 가장 큰 수
print(result[0])  # 가장 작은 수