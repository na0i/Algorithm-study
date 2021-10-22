import sys
sys.stdin = open('1258.txt', 'r')


T = int(input())
for tc in range(T):
    N = int(input())
    store = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N):
            if store[i][j] != 0:
                now_r = i
                now_c = j

                while store[i][now_c] != 0:
                    now_c += 1

                while store[now_r][j] != 0:
                    now_r += 1

                # 행, 열 크기 저장
                result.append((now_r - i, now_c - j))

                # 찾은 박스를 0으로 만들어 다시 세는 일이 없도록 한다.
                for k in range(i, now_r+1):
                    for l in range(j, now_c+1):
                        store[k][l] = 0

    # 행*열(박스 사이즈 저장)
    size = [0] * len(result)
    for s in range(len(result)):
        size[s] = (result[s][0] * result[s][1], s)

    size = sorted(size)

    # 사이즈 순서대로 정렬
    answer = []
    for idx in range(len(size)):
        answer.append(result[size[idx][1]])

    # 동일 사이즈 있을 경우 행이 작은 순으로 정렬
    for a in range(len(answer)-1):
        if answer[a][0] * answer[a][1] == answer[a+1][0] * answer[a+1][1]:
            if answer[a][0] > answer[a+1][0]:
                answer[a], answer[a+1] = answer[a+1], answer[a]
            else:
                continue

    # 정답 출력
    print('#{} {}'.format(tc+1, len(answer)), end=' ')

    for ans in range(len(answer)):
        print(answer[ans][0], end=' ')
        print(answer[ans][1], end=' ')

    print()