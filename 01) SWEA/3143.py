import sys
sys.stdin = open('3143.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = map(str, input().split())

    same = 0
    count = 0
    for i in range(len(A) - len(B) + 1):

        same_idx = 0
        while same_idx < len(B) and A[i+same_idx] == B[same_idx]:
            same_idx += 1

        if same_idx == len(B):
            same += same_idx
            count += 1

    print('#{} {}'.format(tc+1, len(A) - same + count))