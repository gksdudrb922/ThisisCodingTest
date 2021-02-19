## 왕실의 나이트
"""
// problem
8*8 좌표 평면상에서 [(1~8) * (a~h)] 현재 나이트가 위치한 좌표로부터 이동할 수 있는 경우의 수를 구한다.
나이트는 실제 체스 나이트의 움직임과 같다.
// input
현재 나이트가 위치한 좌표 (ex. a1)
// output
나이트가 이동할 수 잇는 경우의 수
"""
# study
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
# O(1)
"""
// learn
기존 dx, dy 두 리스트를 사용하는 것 대신 튜플로 구성된 리스트를 사용할 수 있다.
"""