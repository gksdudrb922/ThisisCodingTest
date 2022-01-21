## 기둥과 보 설치
"""
// problem
프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데,
기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있다.
1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
// input
벽면의 크기 N (5~100)
기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame(행:1~1000, 열:4)
-> build_frame의 열은 (x,y,a,b)로 되어있다.
x,y : 설치 or 삭제할 좌표
a : 0(기둥), 1(보)
b : 0(삭제), 1(설치)
// output
구조물의 상태를 나타내는 2차원 배열(열:3)
-> 열은 (x,y,a)로 되어있다.
x,y : 설치 or 삭제할 좌표
a : 0(기둥), 1(보)
"""


# study
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False  # 아니라면 거짓(False) 반환
        elif stuff == 1:  # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False  # 아니라면 거짓(False) 반환
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:  # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제하는 경우
            answer.remove([x, y, stuff])  # 일단 삭제를 해본 뒤에
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.append([x, y, stuff])  # 가능한 구조물이 아니라면 다시 설치
        if operate == 1:  # 설치하는 경우
            answer.append([x, y, stuff])  # 일단 설치를 해본 뒤에
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.remove([x, y, stuff])  # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer)  # 정렬된 결과를 반환


# O(m3), m=len(build_frame)
"""
// learn
my code에서는 set을 이용해서 시간을 줄일 수 있었다.
그리고 시간이 5초로 주어지기 때문에 O(n3)으로도 가능하다, 1000**3 = 10억 ~ 약 5초
"""
