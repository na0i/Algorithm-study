T = int(input())

triangle = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
triangle.extend([0] * 90)

for t in range(10, 100):
    triangle[t] = triangle[t-5] + triangle[t-1]

for tc in range(T):
    N = int(input())
    print(triangle[N-1])