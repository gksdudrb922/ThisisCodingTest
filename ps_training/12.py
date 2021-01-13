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
def check(answer):
  for i in range(len(answer)):
    x,y,a=answer[i]
    if a==0:
      if not (y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer):
        return False
    else:
      if not ([x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer)):
        return False
  return True

def solution(n, build_frame):
  answer = []

  for i in range(len(build_frame)):
    x,y,a,b=build_frame[i]
    if b==1:
      answer.append([x,y,a])
      if check(answer)==False:
        answer.remove([x,y,a])
    else:
      answer.remove([x,y,a])
      if check(answer)==False:
        answer.append([x,y,a])
  answer=sorted(answer)
  return answer

n=5
build_frame=	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))
# O(n3), n=len(build_frame)