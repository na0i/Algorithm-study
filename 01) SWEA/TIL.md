### 0914

input 파일로 txt를 받을 때 사용하는 코드

```python
import sys
sys.stdin = open('1205.txt', 'r')
```





-------



파이썬 for문 돌리기



for i in `range`(시작, 끝, 간격):

여기서 11을 입력해야 10까지 돈다는 것을 잊지말자



----------



공백없이 입력받기

```python
buildings = list(map(int, input().split()))
```



input 값

```
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 93 203 150 69 19 137 28 174 32 80 64 54 18 0 158 73 173 20 0 102 107 48 50 161 246 145 225 31 0 153 185 157 44 126 153 233 0 201 83 103 191 0 45 0 131 87 97 105 97 209 157 22 0 29 132 74 2 232 44 203 0 51 0 244 212 212 89 53 50 244 207 144 72 143 0 0 
```



print(buildings)

```
[0, 0, 225, 214, 82, 73, 241, 233, 179, 219, 135, 62, 36, 13, 6, 71, 179, 77, 67, 139, 31, 90, 9, 37, 93, 203, 150, 69, 19, 137, 28, 174, 32, 80, 64, 54, 18, 0, 158, 73, 173, 20, 0, 102, 107, 48, 50, 161, 246, 145, 225, 31, 0, 153, 185, 157, 44, 126, 153, 233, 0, 201, 83, 103, 191, 0, 45, 0, 131, 87, 97, 105, 97, 209, 157, 22, 0, 29, 132, 74, 2, 232, 44, 203, 0, 51, 0, 244, 212, 212, 89, 53, 50, 244, 207, 144, 72, 143, 0, 0]
```





--------



max 값 찾기



max 내장함수 이용

```
max(리스트)
```





### 0921

리스트 요소를 하나씩 출력하되 요소 뒤에 띄어쓰기를 추가하고 싶을 때

```python
P = int(input())
    for p in range(P):
    C = int(input())
    print(bus_stop[C], end=' ')
```



--------

이차원 리스트와 같은 다중 리스트에서 깊은 복사를 하기 위해서는

copy.deepcopy를 이용한다



```python
import copy

puzzle_row = [list(map(int, input().split())) for _ in range(N)]
puzzle_col = copy.deepcopy(puzzle_row)
```



### 0923

![image-20210923211945071](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210923211945071.png)

UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 5065: illegal multibyte sequence



input을 맞게 했는데 알 수 없는 오류 발생..!



encoding='UTF8' 을 추가해서 해결

```
import sys
sys.stdin = open('1213.txt', 'r', encoding='UTF8')
```

