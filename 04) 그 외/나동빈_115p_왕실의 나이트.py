import sys
sys.stdin = open('나동빈_115p_왕실의 나이트.txt', 'r')

coordinate = input()

column_key_value = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h':7}
current_r = int(coordinate[1]) - 1
current_c = column_key_value[coordinate[0]]
dr = [-2, -2, -1, -1, 2, 2, 1, 1]
dc = [-1, 1, -2, 2, -1, 1, -2, 2]
cnt = 0
for dir in range(8):
    next_r = current_r + dr[dir]
    next_c = current_c + dc[dir]
    if 0 <= next_r < 8 and 0 <= next_c < 8:
        cnt += 1

print(cnt)