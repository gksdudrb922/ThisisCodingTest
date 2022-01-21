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


# my code
def check(structure):
    for x, y, a in structure:
        if a == 0:
            if not (y == 0 or (x - 1, y, 1) in structure or (x, y, 1) in structure or (x, y - 1, 0) in structure):
                return False
        else:
            if not ((x, y - 1, 0) in structure or (x + 1, y - 1, 0) in structure or (
                    (x - 1, y, 1) in structure and (x + 1, y, 1) in structure)):
                return False
    return True


def solution(n, build_frame):
    structure = set()
    for x, y, a, b in build_frame:
        if b == 0:
            structure.remove((x, y, a))
            if not check(structure):
                structure.add((x, y, a))
        else:
            structure.add((x, y, a))
            if not check(structure):
                structure.remove((x, y, a))

    answer = []
    for x, y, a in structure:
        answer.append([x, y, a])
    answer.sort()
    return answer
# O(m2), m=len(build_frame)
